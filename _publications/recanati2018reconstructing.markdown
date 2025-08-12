---
layout: publication
title: Reconstructing Latent Orderings By Spectral Clustering
authors: Antoine Recanati, Thomas Kerdreux, Alexandre D'Aspremont
conference: Arxiv
year: 2018
bibkey: recanati2018reconstructing
citations: 2
additional_links: [{name: Code, url: 'https://github.com/antrec/mdso'}, {name: Paper,
    url: 'https://arxiv.org/abs/1807.07122'}]
tags: []
short_authors: Antoine Recanati, Thomas Kerdreux, Alexandre D'Aspremont
---
Spectral clustering uses a graph Laplacian spectral embedding to enhance the
cluster structure of some data sets. When the embedding is one dimensional, it
can be used to sort the items (spectral ordering). A number of empirical
results also suggests that a multidimensional Laplacian embedding enhances the
latent ordering of the data, if any. This also extends to circular orderings, a
case where unidimensional embeddings fail. We tackle the task of retrieving
linear and circular orderings in a unifying framework, and show how a latent
ordering on the data translates into a filamentary structure on the Laplacian
embedding. We propose a method to recover it, illustrated with numerical
experiments on synthetic data and real DNA sequencing data. The code and
experiments are available at https://github.com/antrec/mdso.