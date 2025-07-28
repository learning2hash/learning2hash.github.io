---
layout: publication
title: Video Temporal Relationship Mining For Data-efficient Person Re-identification
authors: Siyu Chen, Dengjie Li, Lishuai Gao, Fan Liang, Wei Zhang, Lin Ma
conference: Arxiv
year: 2021
bibkey: chen2021video
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.00549'}]
tags: []
short_authors: Chen et al.
---
This paper is a technical report to our submission to the ICCV 2021 VIPriors
Re-identification Challenge. In order to make full use of the visual inductive
priors of the data, we treat the query and gallery images of the same identity
as continuous frames in a video sequence. And we propose one novel
post-processing strategy for video temporal relationship mining, which not only
calculates the distance matrix between query and gallery images, but also the
matrix between gallery images. The initial query image is used to retrieve the
most similar image from the gallery, then the retrieved image is treated as a
new query to retrieve its most similar image from the gallery. By iteratively
searching for the closest image, we can achieve accurate image retrieval and
finally obtain a robust retrieval sequence.