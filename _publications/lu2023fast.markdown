---
layout: publication
title: Fast Machine Learning Method With Vector Embedding On Orthonormal Basis And
  Spectral Transform
authors: Louis Yu Lu
conference: Arxiv
year: 2023
bibkey: lu2023fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.18424'}]
tags: []
short_authors: Louis Yu Lu
---
This paper presents a novel fast machine learning method that leverages two
techniques: Vector Embedding on Orthonormal Basis (VEOB) and Spectral Transform
(ST). The VEOB converts the original data encoding into a vector embedding with
coordinates projected onto orthonormal bases. The Singular Value Decomposition
(SVD) technique is used to calculate the vector basis and projection
coordinates, leading to an enhanced distance measurement in the embedding space
and facilitating data compression by preserving the projection vectors
associated with the largest singular values. On the other hand, ST transforms
sequence of vector data into spectral space. By applying the Discrete Cosine
Transform (DCT) and selecting the most significant components, it streamlines
the handling of lengthy vector sequences. The paper provides examples of word
embedding, text chunk embedding, and image embedding, implemented in Julia
language with a vector database. It also investigates unsupervised learning and
supervised learning using this method, along with strategies for handling large
data volumes.