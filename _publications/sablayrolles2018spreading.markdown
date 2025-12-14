---
layout: publication
title: Spreading Vectors For Similarity Search
authors: "Alexandre Sablayrolles, Matthijs Douze, Cordelia Schmid, Herv\xE9 J\xE9\
  gou"
conference: Arxiv
year: 2018
bibkey: sablayrolles2018spreading
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.03198'}]
tags: [Distance Metric Learning, Quantization, Evaluation, Similarity Search]
short_authors: Sablayrolles et al.
---
Discretizing multi-dimensional data distributions is a fundamental step of
modern indexing methods. State-of-the-art techniques learn parameters of
quantizers on training data for optimal performance, thus adapting quantizers
to the data. In this work, we propose to reverse this paradigm and adapt the
data to the quantizer: we train a neural net which last layer forms a fixed
parameter-free quantizer, such as pre-defined points of a hyper-sphere. As a
proxy objective, we design and train a neural network that favors uniformity in
the spherical latent space, while preserving the neighborhood structure after
the mapping. We propose a new regularizer derived from the Kozachenko--Leonenko
differential entropy estimator to enforce uniformity and combine it with a
locality-aware triplet loss. Experiments show that our end-to-end approach
outperforms most learned quantization methods, and is competitive with the
state of the art on widely adopted benchmarks. Furthermore, we show that
training without the quantization step results in almost no difference in
accuracy, but yields a generic catalyzer that can be applied with any
subsequent quantizer.