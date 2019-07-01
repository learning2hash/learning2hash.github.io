---
layout: default
title: Tutorial on Locality Sensitive Hashing (LSH) for Audio Indexing and Retrieval
---

## Audio Indexing with Locality Sensitive Hashing (LSH)

Most of the time, to really understand a new technique, its good to just dive straight into coding it up and applying the method to an interesting dataset. In this tutorial we will code our own custom implementation of locality sensitive hashing (LSH) for the *cosine* and *euclidean distances* and evaluate the quality and speed of retrieval compared to a brute-force approach.

#### Obtaining and pre-processing the dataset

We will index and search the [AudioSet](https://research.google.com/audioset/) dataset kindly provided by Google Research. Our goal is to find, for a query audio snippet, similar sounds from the database very very quickly.

The dataset consists of over two million audio segments extracted from a collection of YouTube videos. For each audio snippet the VGG-inspired acoustic model of [Hershey et al.](https://ai.google/research/pubs/pub45611) was used to extract
128 dimensional acoustic features. The feature vectors can be downloaded [here](https://research.google.com/audioset/download.html). Trusty wget can be used to download to your local computer. If you are in the EU, run the following command
and then go and fetch yourself a cup of tea (total size 2.4Gb):

```linux
wget http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```

The dataset comes in the format of Tensorflow [TFRecord](https://www.tensorflow.org/tutorials/load_data/tf_records) files. Our first steps to make
the dataset useable for our purposes will be:

1. Extract the audio features from the TFRecord files
2. Extract the labels for each segment
3. Identify the training, validation and test segments
4. Save the training, validation and test segments in separate Numpy (.npy) files.


