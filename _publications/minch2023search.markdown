---
layout: publication
title: In Search Of The Most Efficient And Memory-saving Visualization Of High Dimensional
  Data
authors: Bartosz Minch
conference: Arxiv
year: 2023
bibkey: minch2023search
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.05455'}]
tags: []
short_authors: Bartosz Minch
---
Interactive exploration of large, multidimensional datasets plays a very
important role in various scientific fields. It makes it possible not only to
identify important structural features and forms, such as clusters of vertices
and their connection patterns, but also to evaluate their interrelationships in
terms of position, distance, shape and connection density. We argue that the
visualization of multidimensional data is well approximated by the problem of
two-dimensional embedding of undirected nearest-neighbor graphs. The size of
complex networks is a major challenge for today's computer systems and still
requires more efficient data embedding algorithms. Existing reduction methods
are too slow and do not allow interactive manipulation. We show that
high-quality embeddings are produced with minimal time and memory complexity.
We present very efficient IVHD algorithms (CPU and GPU) and compare them with
the latest and most popular dimensionality reduction methods. We show that the
memory and time requirements are dramatically lower than for base codes. At the
cost of a slight degradation in embedding quality, IVHD preserves the main
structural properties of the data well with a much lower time budget. We also
present a meta-algorithm that allows the use of any unsupervised data embedding
method in a supervised manner.