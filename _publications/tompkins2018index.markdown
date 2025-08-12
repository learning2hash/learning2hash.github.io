---
layout: publication
title: Index Set Fourier Series Features For Approximating Multi-dimensional Periodic
  Kernels
authors: Anthony Tompkins, Fabio Ramos
conference: Arxiv
year: 2018
bibkey: tompkins2018index
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.04982'}]
tags: []
short_authors: Anthony Tompkins, Fabio Ramos
---
Periodicity is often studied in timeseries modelling with autoregressive
methods but is less popular in the kernel literature, particularly for higher
dimensional problems such as in textures, crystallography, and quantum
mechanics. Large datasets often make modelling periodicity untenable for
otherwise powerful non-parametric methods like Gaussian Processes (GPs) which
typically incur an \(\mathcal\{O\}(N^3)\) computational burden and, consequently,
are unable to scale to larger datasets. To this end we introduce a method
termed *Index Set Fourier Series Features* to tractably exploit
multivariate Fourier series and efficiently decompose periodic kernels on
higher-dimensional data into a series of basis functions. We show that our
approximation produces significantly less predictive error than alternative
approaches such as those based on random Fourier features and achieves better
generalisation on regression problems with periodic data.