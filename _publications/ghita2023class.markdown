---
layout: publication
title: Class Anchor Margin Loss For Content-based Image Retrieval
authors: Alexandru Ghita, Radu Tudor Ionescu
conference: Arxiv
year: 2023
bibkey: ghita2023class
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.00630'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Alexandru Ghita, Radu Tudor Ionescu
---
The performance of neural networks in content-based image retrieval (CBIR) is
highly influenced by the chosen loss (objective) function. The majority of
objective functions for neural models can be divided into metric learning and
statistical learning. Metric learning approaches require a pair mining strategy
that often lacks efficiency, while statistical learning approaches are not
generating highly compact features due to their indirect feature optimization.
To this end, we propose a novel repeller-attractor loss that falls in the
metric learning paradigm, yet directly optimizes for the L2 metric without the
need of generating pairs. Our loss is formed of three components. One leading
objective ensures that the learned features are attracted to each designated
learnable class anchor. The second loss component regulates the anchors and
forces them to be separable by a margin, while the third objective ensures that
the anchors do not collapse to zero. Furthermore, we develop a more efficient
two-stage retrieval system by harnessing the learned class anchors during the
first stage of the retrieval process, eliminating the need of comparing the
query with every image in the database. We establish a set of four datasets
(CIFAR-100, Food-101, SVHN, and Tiny ImageNet) and evaluate the proposed
objective in the context of few-shot and full-set training on the CBIR task, by
using both convolutional and transformer architectures. Compared to existing
objective functions, our empirical evidence shows that the proposed objective
is generating superior and more consistent results.