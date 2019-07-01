---
layout: default
title: Tutorial on Locality Sensitive Hashing (LSH) for Audio Indexing and Retrieval
---

### Audio Indexing with Locality Sensitive Hashing (LSH)

In this tutorial we will code our own custom implementation of locality sensitive hashing (LSH) for the cosine and euclidean distances and evaluate the quality and speed of retrieval compared to a brute-force approach.

#### Obtaining and pre-processing the dataset

We will index and search the [AudioSet](https://research.google.com/audioset/) dataset kindly provided by Google Research. Our goal is to find, for a query audio snippet, similar sounds from the database very very quickly.

The dataset consists of over two million audio segments extracted from a collection of YouTube videos. For each audio snipper the VGG-inpisred acoustic model of [Hershey et al.](https://ai.google/research/pubs/pub45611) was used to extract
128 dimensional acoustic features. The feature vectors can be downloaded [here](https://research.google.com/audioset/download.html). Trusty wet can be used to download to your local computer:

```linux
wget http://storage.googleapis.com/eu_audioset/youtube_corpus/v1/features/features.tar.gz
```
