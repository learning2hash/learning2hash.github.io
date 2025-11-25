---
layout: publication
title: Structured Deep Hashing With Convolutional Neural Networks For Fast Person
  Re-identification
authors: Lin Wu, Yang Wang
conference: Computer Vision and Image Understanding
year: 2017
bibkey: wu2017structured
citations: 75
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.04179'}]
tags: ["Efficiency", "Hashing Methods", "Neural Hashing"]
short_authors: Lin Wu, Yang Wang
---
Given a pedestrian image as a query, the purpose of person re-identification
is to identify the correct match from a large collection of gallery images
depicting the same person captured by disjoint camera views. The critical
challenge is how to construct a robust yet discriminative feature
representation to capture the compounded variations in pedestrian appearance.
To this end, deep learning methods have been proposed to extract hierarchical
features against extreme variability of appearance. However, existing methods
in this category generally neglect the efficiency in the matching stage whereas
the searching speed of a re-identification system is crucial in real-world
applications. In this paper, we present a novel deep hashing framework with
Convolutional Neural Networks (CNNs) for fast person re-identification.
Technically, we simultaneously learn both CNN features and hash functions/codes
to get robust yet discriminative features and similarity-preserving hash codes.
Thereby, person re-identification can be resolved by efficiently computing and
ranking the Hamming distances between images. A structured loss function
defined over positive pairs and hard negatives is proposed to formulate a novel
optimization problem so that fast convergence and more stable optimized
solution can be obtained. Extensive experiments on two benchmarks CUHK03
\cite\{FPNN\} and Market-1501 \cite\{Market1501\} show that the proposed deep
architecture is efficacy over state-of-the-arts.