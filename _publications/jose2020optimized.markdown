---
layout: publication
title: Optimized Feature Space Learning for Generating Efficient Binary Codes for
  Image Retrieval
authors: Jose et al.
conference: 'Signal Processing: Image Communication'
year: 2021
bibkey: jose2020optimized
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.11400'}]
tags: ["Compact-Codes", "Image-Retrieval"]
---
In this paper we propose an approach for learning low dimensional optimized
feature space with minimum intra-class variance and maximum inter-class
variance. We address the problem of high-dimensionality of feature vectors
extracted from neural networks by taking care of the global statistics of
feature space. Classical approach of Linear Discriminant Analysis (LDA) is
generally used for generating an optimized low dimensional feature space for
single-labeled images. Since, image retrieval involves both multi-labeled and
single-labeled images, we utilize the equivalence between LDA and Canonical
Correlation Analysis (CCA) to generate an optimized feature space for
single-labeled images and use CCA to generate an optimized feature space for
multi-labeled images. Our approach correlates the projections of feature
vectors with label vectors in our CCA based network architecture. The neural
network minimize a loss function which maximizes the correlation coefficients.
We binarize our generated feature vectors with the popular Iterative
Quantization (ITQ) approach and also propose an ensemble network to generate
binary codes of desired bit length for image retrieval. Our measurement of mean
average precision shows competitive results on other state-of-the-art
single-labeled and multi-labeled image retrieval datasets.