---
layout: page
title: Taxonomy
description: A taxonomy of machine learning models for hashing.
---
A hashing model takes an input data-point e.g. an image and outputs a sequence of bits (hashcode) representing that image. At the top level, the hashing models can be broadly categorised into two different categories: quantisation and projection. The projection models focus on learning a low-dimensional transformation of the input data in a way that encourages related data-points to be closer together in the new space. In contrast, the quantisation models seek to convert those projections into binary by using a thresholding mechanism. The projection branch can be further divided into data-independent, data-dependent (unsupervised) and data-dependent (supervised) depending on whether the projections are influenced by the distribution of the data or available class-labels.

 * [**Quantisation**](quantisation.html) focus on quantising the real-valued low-dimensional projections of data-points into binary bits by positioning one or more thresholds.
 
 * [**Representational Models of Code**](representational.html) take an abstract
    representation of 
    code as input.  Example representations include token contexts or data flow.
    The resulting model yields a conditional probability distribution over code
    element properties, like the types of variables, and can predict them.

 * [**Pattern Mining Models**](pattern.html) infer, without supervision, a likely latent
    structure within code. These models are an instantiation of clustering
    in the code domain; they can find reusable and human-interpretable patterns.

