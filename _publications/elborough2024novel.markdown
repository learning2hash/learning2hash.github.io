---
layout: publication
title: 'A Novel Application Of Shapley Values For Large Multidimensional Time-series
  Data: Applying Explainable AI To A DNA Profile Classification Neural Network'
authors: Lauren Elborough, Duncan Taylor, Melissa Humphries
conference: Arxiv
year: 2024
bibkey: elborough2024novel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.18156'}]
tags: []
short_authors: Lauren Elborough, Duncan Taylor, Melissa Humphries
---
The application of Shapley values to high-dimensional, time-series-like data
is computationally challenging - and sometimes impossible. For \(N\) inputs the
problem is \(2^N\) hard. In image processing, clusters of pixels, referred to as
superpixels, are used to streamline computations. This research presents an
efficient solution for time-seres-like data that adapts the idea of superpixels
for Shapley value computation. Motivated by a forensic DNA classification
example, the method is applied to multivariate time-series-like data whose
features have been classified by a convolutional neural network (CNN). In DNA
processing, it is important to identify alleles from the background noise
created by DNA extraction and processing. A single DNA profile has \(31,200\)
scan points to classify, and the classification decisions must be defensible in
a court of law. This means that classification is routinely performed by human
readers - a monumental and time consuming process. The application of a CNN
with fast computation of meaningful Shapley values provides a potential
alternative to the classification. This research demonstrates the realistic,
accurate and fast computation of Shapley values for this massive task