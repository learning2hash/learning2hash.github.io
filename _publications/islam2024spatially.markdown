---
layout: publication
title: Spatially Optimized Compact Deep Metric Learning Model for Similarity Search
authors: Islam et al.
conference: Information Fusion
year: 2024
bibkey: islam2024spatially
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.06593'}]
tags: ["Distance-Metric-Learning"]
---
Spatial optimization is often overlooked in many computer vision tasks.
Filters should be able to recognize the features of an object regardless of
where it is in the image. Similarity search is a crucial task where spatial
features decide an important output. The capacity of convolution to capture
visual patterns across various locations is limited. In contrast to
convolution, the involution kernel is dynamically created at each pixel based
on the pixel value and parameters that have been learned. This study
demonstrates that utilizing a single layer of involution feature extractor
alongside a compact convolution model significantly enhances the performance of
similarity search. Additionally, we improve predictions by using the GELU
activation function rather than the ReLU. The negligible amount of weight
parameters in involution with a compact model with better performance makes the
model very useful in real-world implementations. Our proposed model is below 1
megabyte in size. We have experimented with our proposed methodology and other
models on CIFAR-10, FashionMNIST, and MNIST datasets. Our proposed method
outperforms across all three datasets.