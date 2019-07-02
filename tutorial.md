---
layout: default
title: Tutorial on Locality Sensitive Hashing (LSH) for Audio Indexing and Retrieval
---

## Audio Indexing with Locality Sensitive Hashing (LSH)

In this tutorial we will build a high-performance system to quickly retrieve related YouTube videos in a databae of over 2 million videos. Retrieval will be based on discriminative features attracted from the audio channel of the videos (10 second audio snippet). Some random videos from this collection are included below:

<iframe style="display:inline" width="100" height="75" src="https://www.youtube.com/embed/o0UkYQyz7Go" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe style="display:inline" width="100" height="75" src="https://www.youtube.com/embed/o0UkYQyz7Go" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe style="display:inline" width="100" height="75" src="https://www.youtube.com/embed/o0UkYQyz7Go" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe style="display:inline" width="100" height="75" src="https://www.youtube.com/embed/o0UkYQyz7Go" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

More information on the dataset characteristics can be found [here](https://research.google.com/audioset/dataset/index.html).

### Getting our hands dirty

Most of the time, to really understand a new technique, it's a good idea to just dive straight into coding it up and applying the method to an interesting dataset. In this tutorial we will code our own custom implementation of locality sensitive hashing (LSH) for the [cosine](https://en.wikipedia.org/wiki/Cosine_similarity) and [euclidean distances](https://en.wikipedia.org/wiki/Euclidean_distance) and evaluate the quality and speed of retrieval compared to a brute-force approach.

We'll even go one step further and show how we can instill a degree of data-dependence into the hashcodes by [leveraging available labels](https://link.springer.com/chapter/10.1007/978-3-319-16354-3_15).

No prior knowledge of acoustics is assumed.

Once you've completed this tutorial you'll also be in a position to wield the power of LSH on any type of dataset of your choice, and you'll be in a great position to start exploring [state-of-the-art methods](https://learning2hash.github.io/papers.html) that learn the distribution of data when indexing the database.

Specifically we will investigate, and seek answers to the following questions:

1. How do we effectively aggregate 1 second long audio embeddings to form a single audio embedding representing a 10 second long segment?
2. Which LSH parameters are optimal for audio retrieval?
3. Can we outperform brute-force search in terms of query-time, and if so by how much?
4. How does the quality of nearest neighbours compare to brute-force search?

For ease of explanation, our tool of choice in this tutorial will be [Python 3](https://www.python.org/download/releases/3.0/), however we should really code this in low-level C (with a Python wrapper perhaps) (future work!).

### Obtaining and pre-processing the AudioSet dataset

We will index and search the [AudioSet](https://research.google.com/audioset/) dataset kindly provided by Google Research. Our goal is to find, for a query audio snippet, similar sounds from the database very very quickly.

The dataset consists of over two million audio segments extracted from a collection of YouTube videos. For each audio snippet the VGG-inspired acoustic model of [Hershey et al.](https://ai.google/research/pubs/pub45611) was used to extract
128 dimensional acoustic features. The feature vectors can be downloaded [here](https://research.google.com/audioset/download.html). The trusty wget command can be used to download to your local computer. If you are in the EU, run the following command
and then go and fetch yourself a cup, or many cups of tea (total size 2.4Gb, an hour or two on a fast internet connection):

```unix
wget http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```

To restart a partial or interrupted download you can use the -c flag:

```unix
wget -c http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```

The dataset comes in the format of Tensorflow [TFRecord](https://www.tensorflow.org/tutorials/load_data/tf_records) files. Our first steps to make the dataset useable for our purposes will be:

1. Extract the 128 dimensional audio features from the TFRecord files and write to a numpy pickle file (.npy)
2. Extract the relevant metadata for each audio segment (start time, end time, labels).
3. Take a small portion (10%) of the training dataset and break out into an independent validation dataset (for parameter tuning)

The training dataset will act as the database that we will index with LSH. The validation dataset is handy for determining the main LSH parameters
(L, the number of hashtables and K, the number of bits per hash key). We will tune these later to maximise our performance metrics (recall and
precision). The test dataset will form our queries that will be used to return matches
from the database.

For a given query sound (e.g. a bird song) we hope similar sounds (and therfore associated videos) from the database will be returned! Without further ado, let's get started on extracting
our audio feature-set!

#### Extracting data from the TFRecord files

Having downloaded the feature files, we will have two directories (unbal and eval) containing many TFRecord files. The audio features and associated metadata are contained in those TFRecord
files and our first task is to extract the data into .npy and .csv files that will be easier used within our Python code and other frameworks (PyTorch, Scikit-learn etc).

The following code snippet performs the extraction, in this case for the eval features (simply uncomment the relevant lines to also extract the training data):

```python
'''
Code to read the Google Audioset dataset TFRecord format and create numpy feature files and csv formatted metadata files for the training and test splits.

To use this script please extract unbal_train and eval TFRecords to ./unbal_train and ./eval directories within the same directory as this script.
'''

import tensorflow as tf
from os import listdir
from os.path import isfile, join
import numpy as np
import os.path as path
import csv

'''
Uncomment the following line to generate the unbalanced training dataset (our database)
'''
#onlyfiles=[join("./unbal_train/", f) for f in listdir("./unbal_train/") if isfile(join("./unbal_train/", f))]
#csv_file="./train_metadata.csv"
#features_filename=path.join("./train_features.npy")
#metadata_filename=path.join("./train_metadata.csv")
#fp1=np.memmap(features_filename, dtype='float32', mode-'w+', shape=(20326484,128))

'''
Uncomment the following line to generate the query dataset (our query set)
'''
onlyfiles=[join("./eval/", f) for f in listdir("./eval/") if isfile(join("./eval/", f))]
csv_file="./eval_metadata.csv"
features_filename=path.join("./eval_features.npy")
metadata_filename=path.join("./eval_metadata.csv")
fp1=np.memmap(features_filename, dtype='float32', mode-'w+', shape=(202439,128))


```

#### DeepAggregationNet: Training a small neural network to aggregate 1 second audio embeddings to a 10 second word embedding

For each 10 second long YouTube video, the AudioSet dataset provides 10 128 dimensional acoustic features (each segment represents 1 second of audio). To represent the entire video as one
embedding vector we will train a small neural network in PyTorch to aggregate the 10 word embeddings per video to give a single aggregate word embedding. Our weapon of choice here will be
a convolutional neural network (CNN).
