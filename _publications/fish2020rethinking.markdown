---
layout: publication
title: Rethinking Movie Genre Classification With Fine-grained Semantic Clustering
authors: Edward Fish, Jon Weinbren, Andrew Gilbert
conference: Arxiv
year: 2020
bibkey: fish2020rethinking
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.02639'}]
tags: ["Datasets"]
short_authors: Edward Fish, Jon Weinbren, Andrew Gilbert
---
Movie genre classification is an active research area in machine learning.
However, due to the limited labels available, there can be large semantic
variations between movies within a single genre definition. We expand these
'coarse' genre labels by identifying 'fine-grained' semantic information within
the multi-modal content of movies. By leveraging pre-trained 'expert' networks,
we learn the influence of different combinations of modes for multi-label genre
classification. Using a contrastive loss, we continue to fine-tune this
'coarse' genre classification network to identify high-level intertextual
similarities between the movies across all genre labels. This leads to a more
'fine-grained' and detailed clustering, based on semantic similarities while
still retaining some genre information. Our approach is demonstrated on a newly
introduced multi-modal 37,866,450 frame, 8,800 movie trailer dataset,
MMX-Trailer-20, which includes pre-computed audio, location, motion, and image
embeddings.