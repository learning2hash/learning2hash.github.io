---
layout: publication
title: Low-rank Toeplitz Matrix Estimation Via Random Ultra-sparse Rulers
authors: Hannah Lawrence, Jerry Li, Cameron Musco, Christopher Musco
conference: Arxiv
year: 2019
bibkey: lawrence2019low
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08015'}]
tags: []
short_authors: Lawrence et al.
---
We study how to estimate a nearly low-rank Toeplitz covariance matrix \(T\)
from compressed measurements. Recent work of Qiao and Pal addresses this
problem by combining sparse rulers (sparse linear arrays) with frequency
finding (sparse Fourier transform) algorithms applied to the Vandermonde
decomposition of \(T\). Analytical bounds on the sample complexity are shown,
under the assumption of sufficiently large gaps between the frequencies in this
decomposition. In this work, we introduce random ultra-sparse rulers and
propose an improved approach based on these objects. Our random rulers
effectively apply a random permutation to the frequencies in \(T\)'s Vandermonde
decomposition, letting us avoid frequency gap assumptions and leading to
improved sample complexity bounds. In the special case when \(T\) is circulant,
we theoretically analyze the performance of our method when combined with
sparse Fourier transform algorithms based on random hashing. We also show
experimentally that our ultra-sparse rulers give significantly more robust and
sample efficient estimation then baseline methods.