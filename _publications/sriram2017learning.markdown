---
layout: publication
title: Learning Autoencoded Radon Projections
authors: Aditya Sriram, Shivam Kalra, H. R. Tizhoosh, Shahryar Rahnamayan
conference: 2017 IEEE Symposium Series on Computational Intelligence (SSCI)
year: 2017
bibkey: sriram2017learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01247'}]
tags: [Evaluation, Tools & Libraries, Datasets, Survey Paper]
short_authors: Sriram et al.
---
Autoencoders have been recently used for encoding medical images. In this
study, we design and validate a new framework for retrieving medical images by
classifying Radon projections, compressed in the deepest layer of an
autoencoder. As the autoencoder reduces the dimensionality, a multilayer
perceptron (MLP) can be employed to classify the images. The integration of MLP
promotes a rather shallow learning architecture which makes the training
faster. We conducted a comparative study to examine the capabilities of
autoencoders for different inputs such as raw images, Histogram of Oriented
Gradients (HOG) and normalized Radon projections. Our framework is benchmarked
on IRMA dataset containing \(14,410\) x-ray images distributed across \(57\)
different classes. Experiments show an IRMA error of \(313\) (equivalent to
\(\approx 82%\) accuracy) outperforming state-of-the-art works on retrieval from
IRMA dataset using autoencoders.