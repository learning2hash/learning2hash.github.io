---
layout: publication
title: Rotation Invariant Angular Descriptor Via A Bandlimited Gaussian-like Kernel
authors: Michael T. McCann, Matthew Fickus, Jelena Kovacevic
conference: Arxiv
year: 2016
bibkey: mccann2016rotation
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.02753'}]
tags: []
short_authors: Michael T. McCann, Matthew Fickus, Jelena Kovacevic
---
We present a new smooth, Gaussian-like kernel that allows the kernel density
estimate for an angular distribution to be exactly represented by a finite
number of its Fourier series coefficients. Distributions of angular quantities,
such as gradients, are a central part of several state-of-the-art image
processing algorithms, but these distributions are usually described via
histograms and therefore lack rotation invariance due to binning artifacts.
Replacing histograming with kernel density estimation removes these binning
artifacts and can provide a finite-dimensional descriptor of the distribution,
provided that the kernel is selected to be bandlimited. In this paper, we
present a new band-limited kernel that has the added advantage of being
Gaussian-like in the angular domain. We then show that it compares favorably to
gradient histograms for patch matching, person detection, and texture
segmentation.