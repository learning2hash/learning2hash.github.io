---
layout: publication
title: Saliency Weighted Convolutional Features For Instance Search
authors: Eva Mohedano, Kevin Mcguinness, Xavier Giro-i-nieto, Noel E. O'connor
conference: 2018 International Conference on Content-Based Multimedia Indexing (CBMI)
year: 2018
bibkey: mohedano2017saliency
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.10795'}]
tags: []
short_authors: Mohedano et al.
---
This work explores attention models to weight the contribution of local
convolutional representations for the instance search task. We present a
retrieval framework based on bags of local convolutional features (BLCF) that
benefits from saliency weighting to build an efficient image representation.
The use of human visual attention models (saliency) allows significant
improvements in retrieval performance without the need to conduct region
analysis or spatial verification, and without requiring any feature fine
tuning. We investigate the impact of different saliency models, finding that
higher performance on saliency benchmarks does not necessarily equate to
improved performance when used in instance search tasks. The proposed approach
outperforms the state-of-the-art on the challenging INSTRE benchmark by a large
margin, and provides similar performance on the Oxford and Paris benchmarks
compared to more complex methods that use off-the-shelf representations. The
source code used in this project is available at
https://imatge-upc.github.io/salbow/