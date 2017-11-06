---
layout: page
title: Taxonomy
description: A taxonomy of machine learning models for hashing.
---
A hashing model takes an input data-point e.g. an image or document, and outputs a sequence of bits (hashcode) representing that data-point. At the top level, the hashing models can be broadly categorised into two different categories: *quantisation* and *projection*. The projection models focus on learning a low-dimensional transformation of the input data in a way that encourages related data-points to be closer together in the new space. In contrast, the quantisation models seek to convert those projections into binary by using a thresholding mechanism. The projection branch can be further divided into data-independent, data-dependent (unsupervised) and data-dependent (supervised) depending on whether the projections are influenced by the distribution of the data or available class-labels.

 * [**Quantisation Models**](quantisation.html) focus on quantising the real-valued low-dimensional projections of data-points into binary bits by positioning one or more thresholds along a projected dimension.
 
 * [**Data Independent Projection Models**](independent.html) these methods fracture the input feature space using randomly drawn hyperplanes independently of the data distribution. Given the random nature of the learning procedure they are the fastest models at training time but suffer from the disadvantage of requiring long hashcodes and many hashtables to attain a reasonable level of retrieval effectiveness.
 
 * [**Supervised Projection Models**](supervised.html) include models that leverage available supervision in the form of class labels, must-link or cannot-link constraints between data-point pairs, triplet-based relational information etc. The models use this supervision to ensure that only related data-points are hashed to the same buckets. These models typically exhibit the highest retrieval effectiveness but suffer the disadvantage of requiring manual labels which can be challenging to collect.

 * [**Unsupervised Projection Models**](unsupervised.html) are models that account for the distribution of the data in an unsupervised manner (i.e. they do not need manually acquired labels). They typically achieve this by using techniques that factorise the data covariance matrix or cluster related data-points into groups. These models generally exhibit a good retrieval effectiveness lying somewhere between the data independent and supervised models, but suffer from the considerable advantage of being computationally expensive at training time (due to the matrix factorisation component).
