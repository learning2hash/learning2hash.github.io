---
layout: page
title: Taxonomy
description: A taxonomy of machine learning models for hashing.
---
A hashing model takes an input data-point e.g. an image or document, and outputs a sequence of bits (hashcode) representing that data-point. At the top level, the hashing models can be broadly categorised into two different categories: quantisation and projection. The projection models focus on learning a low-dimensional transformation of the input data in a way that encourages related data-points to be closer together in the new space. In contrast, the quantisation models seek to convert those projections into binary by using a thresholding mechanism. The projection branch can be further divided into data-independent, data-dependent (unsupervised) and data-dependent (supervised) depending on whether the projections are influenced by the distribution of the data or available class-labels.

 * [**Quantisation**](quantisation.html) focus on quantising the real-valued low-dimensional projections of data-points into binary bits by positioning one or more thresholds along a projected dimension.
 
 * [**Data Independent Projection**](independent.html) these methods 
 
 * [**Supervised Projection**](supervised.html) include models that leverage available supervision in the form of class labels, pairwise must-link or cannot-link constraints, triplet-based information etc. These models typically exhibit the highest retrieval effectiveness but suffer the disadvantage of requiring manual labels which can be difficult to collect.

 * [**Unsupervised Projection**](unsupervised.html) 
