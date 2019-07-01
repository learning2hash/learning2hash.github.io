---
layout: default
title: Tutorial on Locality Sensitive Hashing (LSH) for Audio Indexing and Retrieval
---

## Audio Indexing with Locality Sensitive Hashing (LSH)

### Getting our hands dirty

Most of the time, to really understand a new technique, it's a good idea to just dive straight into coding it up and applying the method to an interesting dataset. In this tutorial we will code our own custom implementation of locality sensitive hashing (LSH) for the [cosine](https://en.wikipedia.org/wiki/Cosine_similarity) and [euclidean distances](https://en.wikipedia.org/wiki/Euclidean_distance) and evaluate the quality and speed of retrieval compared to a brute-force approach.

Once you've completed this tutorial you'll be in a position to wield the power of LSH on any type of dataset of your choice, and you'll be in a great position to start exploring [state-of-the-art methods](https://learning2hash.github.io/papers.html) that learn the distribution of data when indexing the database.

Specifically we will investigate, and seek answers to the following questions:

1. Which LSH parameters are optimal for the audio retrieval?
2. Can we outperform brute-force search in terms of query-time, and if so by how much?
3. How does the quality of nearest neighbours compare to brute-force search?

For ease of explaination, our tool of choice will be Python3, however we should really code this in low-level C (with a Python wrapper perhaps).

### Obtaining and pre-processing the AudioSet dataset

We will index and search the [AudioSet](https://research.google.com/audioset/) dataset kindly provided by Google Research. Our goal is to find, for a query audio snippet, similar sounds from the database very very quickly.

The dataset consists of over two million audio segments extracted from a collection of YouTube videos. For each audio snippet the VGG-inspired acoustic model of [Hershey et al.](https://ai.google/research/pubs/pub45611) was used to extract
128 dimensional acoustic features. The feature vectors can be downloaded [here](https://research.google.com/audioset/download.html). Trusty wget can be used to download to your local computer. If you are in the EU, run the following command
and then go and fetch yourself a cup, or many cups of tea (total size 2.4Gb, an hour or two on a fast internet connection):

```linux
wget http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```

To restart a partial or interrupted download you can use the -c flag:

```linux
wget -c http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```

The dataset comes in the format of Tensorflow [TFRecord](https://www.tensorflow.org/tutorials/load_data/tf_records) files. Our first steps to make
the dataset useable for our purposes will be:

1. Extract the audio features from the TFRecord files
2. Extract the labels for each segment
3. Identify the training, validation and test segments
4. Save the training, validation and test segments in separate Numpy (.npy) files.

The training dataset will act as the database that we will index with LSH. The validation dataset is handy for determining the main LSH parameters
(L, the number of hashtables and K, the number of bits per hash key). We will tune these later to maximise our performance metrics (recall and
precision). The test dataset will form our queries that will be used to return matches
from the database.

For a given query sound (e.g. a bird song) we hope similar sounds from the database will be returned! Without further ado, let's get started on extracting
our featureset!

