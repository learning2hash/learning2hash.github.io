---
layout: publication
title: Convolutional Embedding for Edit Distance
authors: Dai et al.
conference: Proceedings of the 43rd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2020
bibkey: dai2020convolutional
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.11692'}]
tags: ["SIGIR"]
---
Edit-distance-based string similarity search has many applications such as
spell correction, data de-duplication, and sequence alignment. However,
computing edit distance is known to have high complexity, which makes string
similarity search challenging for large datasets. In this paper, we propose a
deep learning pipeline (called CNN-ED) that embeds edit distance into Euclidean
distance for fast approximate similarity search. A convolutional neural network
(CNN) is used to generate fixed-length vector embeddings for a dataset of
strings and the loss function is a combination of the triplet loss and the
approximation error. To justify our choice of using CNN instead of other
structures (e.g., RNN) as the model, theoretical analysis is conducted to show
that some basic operations in our CNN model preserve edit distance.
Experimental results show that CNN-ED outperforms data-independent CGK
embedding and RNN-based GRU embedding in terms of both accuracy and efficiency
by a large margin. We also show that string similarity search can be
significantly accelerated using CNN-based embeddings, sometimes by orders of
magnitude.