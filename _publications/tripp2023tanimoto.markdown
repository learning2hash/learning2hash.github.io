---
layout: publication
title: Tanimoto Random Features For Scalable Molecular Machine Learning
authors: "Austin Tripp, Sergio Bacallado, Sukriti Singh, Jos\xE9 Miguel Hern\xE1ndez-Lobato"
conference: Arxiv
year: 2023
bibkey: tripp2023tanimoto
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14809'}]
tags: ["Distance Metric Learning"]
short_authors: Tripp et al.
---
The Tanimoto coefficient is commonly used to measure the similarity between
molecules represented as discrete fingerprints, either as a distance metric or
a positive definite kernel. While many kernel methods can be accelerated using
random feature approximations, at present there is a lack of such
approximations for the Tanimoto kernel. In this paper we propose two kinds of
novel random features to allow this kernel to scale to large datasets, and in
the process discover a novel extension of the kernel to real-valued vectors. We
theoretically characterize these random features, and provide error bounds on
the spectral norm of the Gram matrix. Experimentally, we show that these random
features are effective at approximating the Tanimoto coefficient of real-world
datasets and are useful for molecular property prediction and optimization
tasks.