---
layout: page
title: Taxonomy
description: A taxonomy of machine learning models for hashing-based approximate nearest neighbour search.
---

### Taxonomy of Hashing Models in Machine Learning

When we talk about hashing models, we're referring to methods that transform input data—like an image or document—into a unique sequence of bits known as a *hashcode*. These models are essential for speeding up approximate nearest neighbor search, making them pivotal for large-scale machine learning tasks. 

Hashing models can be grouped into two primary categories: **Projection** and **Quantization**.

- **Projection Models** aim to create low-dimensional representations of input data where similar items are closer together in a transformed space. These models can be further broken down into data-independent, data-dependent (unsupervised), and data-dependent (supervised) approaches.
  
- **Quantization Models** take those projections and convert them into binary hashcodes by applying thresholds, making them efficient for retrieval tasks.

#### Diving Deeper into the Taxonomy:
1. **[Quantization Models](quantisation.html):** These models quantize continuous low-dimensional projections into binary bits using one or more thresholds. They focus on translating numerical data into binary representations for faster searches.
   
2. **[Data-Independent Projection Models](independent.html):** By using randomly generated hyperplanes, these models divide the input feature space without considering the data's distribution. While incredibly fast during training, they require longer hashcodes and multiple hashtables to achieve effective retrieval.

3. **[Supervised Projection Models](supervised.html):** Leveraging labeled data such as class labels or pairwise constraints, these models learn to hash related data points into the same buckets. They offer the highest retrieval performance, though they rely on manually collected labels, which can be a hurdle.

4. **[Unsupervised Projection Models](unsupervised.html):** These models adapt to the data’s inherent distribution without requiring labels. By using techniques like covariance matrix factorization or clustering, they strike a balance between data-independent and supervised models in terms of performance, but come with higher computational costs during training.
