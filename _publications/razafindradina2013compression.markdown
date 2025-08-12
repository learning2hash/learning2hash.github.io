---
layout: publication
title: Compression D'images Par SVD Et Sur-approximation Des Composantes De Chrominance
authors: Henri Bruno Razafindradina, Paul Auguste Randriamitantsoa, Nicolas Raft Razafindrakoto
conference: Arxiv
year: 2013
bibkey: razafindradina2013compression
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1308.0608'}]
tags: ["Efficiency", "Image Retrieval", "Memory Efficiency"]
short_authors: Henri Bruno Razafindradina, Paul Auguste Randriamitantsoa, Nicolas
  Raft Razafindrakoto
---
This paper gives a new scheme of colour image compression related to singular
values matrix approximation. The image has to be converted in luminance /
chrominance space before being processed like JPEG standard 4 : 2 : 0. Our
approach is first based on a chrominance sub-sampling, then an over estimation
of its singular values. Instead of keeping only the k first singular values for
the 3 components R, G and B, we hold k first coefficients for the Y component
and only k' (k' <= k) coefficients for 2 components Cb and Cr. Results show
that for 512 x 512 pixels that, from k = 40 corresponding in an average
distortion of 30 dB and a ratio of 15 : 1, the restored image has good quality.
The algorithm allows a significant speed gain by sub-sampling too.