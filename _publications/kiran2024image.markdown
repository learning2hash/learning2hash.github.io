---
layout: publication
title: Image Retrieval Methods In The Dissimilarity Space
authors: Madhu Kiran, Kartikey Vishnu, Rafael M. O. Cruz, Eric Granger
conference: Arxiv
year: 2024
bibkey: kiran2024image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.08618'}]
tags: [Neural Hashing, Datasets, Image Retrieval, Distance Metric Learning, Evaluation]
short_authors: Kiran et al.
---
Image retrieval methods rely on metric learning to train backbone feature
extraction models that can extract discriminant queries and reference (gallery)
feature representations for similarity matching. Although state-of-the-art
accuracy has improved considerably with the advent of deep learning (DL) models
trained on large datasets, image retrieval remains challenging in many
real-world video analytics and surveillance applications, e.g., person
re-identification. Using the Euclidean space for matching limits the
performance in real-world applications due to the curse of dimensionality,
overfitting, and sensitivity to noisy data.
  We argue that the feature dissimilarity space is more suitable for similarity
matching, and propose a dichotomy transformation to project query and reference
embeddings into a single embedding in the dissimilarity space.
  We also advocate for end-to-end training of a backbone and binary
classification models for pair-wise matching. As opposed to comparing the
distance between queries and reference embeddings, we show the benefits of
classifying the single dissimilarity space embedding (as similar or
dissimilar), especially when trained end-to-end. We propose a method to train
the max-margin classifier together with the backbone feature extractor by
applying constraints to the L2 norm of the classifier weights along with the
hinge loss.
  Our extensive experiments on challenging image retrieval datasets and using
diverse feature extraction backbones highlight the benefits of similarity
matching in the dissimilarity space. In particular, when jointly training the
feature extraction backbone and regularised classifier for matching, the
dissimilarity space provides a higher level of accuracy.