---
layout: publication
title: An Universal Image Attractiveness Ranking Framework
authors: Ning Ma, Alexey Volkov, Aleksandr Livshits, Pawel Pietrusinski, Houdong Hu,
  Mark Bolin
conference: 2019 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: ma2018universal
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.00309'}]
tags: []
short_authors: Ma et al.
---
We propose a new framework to rank image attractiveness using a novel
pairwise deep network trained with a large set of side-by-side multi-labeled
image pairs from a web image index. The judges only provide relative ranking
between two images without the need to directly assign an absolute score, or
rate any predefined image attribute, thus making the rating more intuitive and
accurate. We investigate a deep attractiveness rank net (DARN), a combination
of deep convolutional neural network and rank net, to directly learn an
attractiveness score mean and variance for each image and the underlying
criteria the judges use to label each pair. The extension of this model
(DARN-V2) is able to adapt to individual judge's personal preference. We also
show the attractiveness of search results are significantly improved by using
this attractiveness information in a real commercial search engine. We evaluate
our model against other state-of-the-art models on our side-by-side web test
data and another public aesthetic data set. With much less judgments (1M vs
50M), our model outperforms on side-by-side labeled data, and is comparable on
data labeled by absolute score.