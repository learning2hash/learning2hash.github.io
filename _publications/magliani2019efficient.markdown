---
layout: publication
title: An Efficient Approximate kNN Graph Method for Diffusion on Image Retrieval
authors: Magliani et al.
conference: Lecture Notes in Computer Science
year: 2019
bibkey: magliani2019efficient
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08668'}]
tags: []
---
The application of the diffusion in many computer vision and artificial
intelligence projects has been shown to give excellent improvements in
performance. One of the main bottlenecks of this technique is the quadratic
growth of the kNN graph size due to the high-quantity of new connections
between nodes in the graph, resulting in long computation times. Several
strategies have been proposed to address this, but none are effective and
efficient. Our novel technique, based on LSH projections, obtains the same
performance as the exact kNN graph after diffusion, but in less time
(approximately 18 times faster on a dataset of a hundred thousand images). The
proposed method was validated and compared with other state-of-the-art on
several public image datasets, including Oxford5k, Paris6k, and Oxford105k.