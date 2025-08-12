---
layout: publication
title: 'K-origins: Better Colour Quantification For Neural Networks'
authors: Lewis Mason, Mark Martinez
conference: Arxiv
year: 2024
bibkey: mason2024k
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.02281'}]
tags: []
short_authors: Lewis Mason, Mark Martinez
---
K-Origins is a neural network layer designed to improve image-based network
performances when learning colour, or intensities, is beneficial. Over 250
encoder-decoder convolutional networks are trained and tested on 16-bit
synthetic data, demonstrating that K-Origins improves semantic segmentation
accuracy in two scenarios: object detection with low signal-to-noise ratios,
and segmenting multiple objects that are identical in shape but vary in colour.
K-Origins generates output features from the input features, \(\textbf\{X\}\), by
the equation \(\textbf\{Y\}_k = \textbf\{X\}-\textbf\{J\}\cdot w_k\) for each trainable
parameter \(w_k\), where \(\textbf\{J\}\) is a matrix of ones. Additionally, networks
with varying receptive fields were trained to determine optimal network depths
based on the dimensions of target classes, suggesting that receptive field
lengths should exceed object sizes. By ensuring a sufficient receptive field
length and incorporating K-Origins, we can achieve better semantic network
performance.