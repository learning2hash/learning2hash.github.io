---
layout: publication
title: A Multimodal Approach Towards Emotion Recognition Of Music Using Audio And
  Lyrical Content
authors: Aniruddha Bhattacharya, K. V. Kadambari
conference: Arxiv
year: 2018
bibkey: bhattacharya2018multimodal
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.05760'}]
tags: ["Datasets", "Evaluation"]
short_authors: Aniruddha Bhattacharya, K. V. Kadambari
---
We propose MoodNet - A Deep Convolutional Neural Network based architecture
to effectively predict the emotion associated with a piece of music given its
audio and lyrical content.We evaluate different architectures consisting of
varying number of two-dimensional convolutional and subsampling layers,followed
by dense layers.We use Mel-Spectrograms to represent the audio content and word
embeddings-specifically 100 dimensional word vectors, to represent the textual
content represented by the lyrics.We feed input data from both modalities to
our MoodNet architecture.The output from both the modalities are then fused as
a fully connected layer and softmax classfier is used to predict the category
of emotion.Using F1-score as our metric,our results show excellent performance
of MoodNet over the two datasets we experimented on-The MIREX Multimodal
dataset and the Million Song Dataset.Our experiments reflect the hypothesis
that more complex models perform better with more training data.We also observe
that lyrics outperform audio as a better expressed modality and conclude that
combining and using features from multiple modalities for prediction tasks
result in superior performance in comparison to using a single modality as
input.