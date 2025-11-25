---
layout: publication
title: Minimum-distortion Embedding
authors: Akshay Agrawal, Alnur Ali, Stephen Boyd
conference: Arxiv
year: 2021
bibkey: agrawal2021minimum
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.02559'}]
tags: ["Distance Metric Learning", "Tools & Libraries"]
short_authors: Akshay Agrawal, Alnur Ali, Stephen Boyd
---
We consider the vector embedding problem. We are given a finite set of items,
with the goal of assigning a representative vector to each one, possibly under
some constraints (such as the collection of vectors being standardized, i.e.,
having zero mean and unit covariance). We are given data indicating that some
pairs of items are similar, and optionally, some other pairs are dissimilar.
For pairs of similar items, we want the corresponding vectors to be near each
other, and for dissimilar pairs, we want the corresponding vectors to not be
near each other, measured in Euclidean distance. We formalize this by
introducing distortion functions, defined for some pairs of the items. Our goal
is to choose an embedding that minimizes the total distortion, subject to the
constraints. We call this the minimum-distortion embedding (MDE) problem.
  The MDE framework is simple but general. It includes a wide variety of
embedding methods, such as spectral embedding, principal component analysis,
multidimensional scaling, dimensionality reduction methods (like Isomap and
UMAP), force-directed layout, and others. It also includes new embeddings, and
provides principled ways of validating historical and new embeddings alike.
  We develop a projected quasi-Newton method that approximately solves MDE
problems and scales to large data sets. We implement this method in PyMDE, an
open-source Python package. In PyMDE, users can select from a library of
distortion functions and constraints or specify custom ones, making it easy to
rapidly experiment with different embeddings. Our software scales to data sets
with millions of items and tens of millions of distortion functions. To
demonstrate our method, we compute embeddings for several real-world data sets,
including images, an academic co-author network, US county demographic data,
and single-cell mRNA transcriptomes.