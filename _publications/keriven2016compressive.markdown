---
layout: publication
title: Compressive K-means
authors: "Nicolas Keriven, Nicolas Tremblay, Yann Traonmilin, R\xE9mi Gribonval"
conference: 2017 IEEE International Conference on Acoustics, Speech and Signal Processing
  (ICASSP)
year: 2017
bibkey: keriven2016compressive
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.08738'}]
tags: ["ICASSP"]
short_authors: Keriven et al.
---
The Lloyd-Max algorithm is a classical approach to perform K-means
clustering. Unfortunately, its cost becomes prohibitive as the training dataset
grows large. We propose a compressive version of K-means (CKM), that estimates
cluster centers from a sketch, i.e. from a drastically compressed
representation of the training dataset. We demonstrate empirically that CKM
performs similarly to Lloyd-Max, for a sketch size proportional to the number
of cen-troids times the ambient dimension, and independent of the size of the
original dataset. Given the sketch, the computational complexity of CKM is also
independent of the size of the dataset. Unlike Lloyd-Max which requires several
replicates, we further demonstrate that CKM is almost insensitive to
initialization. For a large dataset of 10^7 data points, we show that CKM can
run two orders of magnitude faster than five replicates of Lloyd-Max, with
similar clustering performance on artificial data. Finally, CKM achieves lower
classification errors on handwritten digits classification.