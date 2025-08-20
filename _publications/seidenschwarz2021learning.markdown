---
layout: publication
title: Learning Intra-batch Connections For Deep Metric Learning
authors: "Jenny Seidenschwarz, Ismail Elezi, Laura Leal-Taix\xE9"
conference: Arxiv
year: 2021
bibkey: seidenschwarz2021learning
citations: 23
additional_links: [{name: Code, url: 'https://github.com/dvl-tum/intra_batch_connections.'},
  {name: Paper, url: 'https://arxiv.org/abs/2102.07753'}]
tags: [Distance Metric Learning, Image Retrieval, Datasets]
short_authors: "Jenny Seidenschwarz, Ismail Elezi, Laura Leal-Taix\xE9"
---
The goal of metric learning is to learn a function that maps samples to a
lower-dimensional space where similar samples lie closer than dissimilar ones.
Particularly, deep metric learning utilizes neural networks to learn such a
mapping. Most approaches rely on losses that only take the relations between
pairs or triplets of samples into account, which either belong to the same
class or two different classes. However, these methods do not explore the
embedding space in its entirety. To this end, we propose an approach based on
message passing networks that takes all the relations in a mini-batch into
account. We refine embedding vectors by exchanging messages among all samples
in a given batch allowing the training process to be aware of its overall
structure. Since not all samples are equally important to predict a decision
boundary, we use an attention mechanism during message passing to allow samples
to weigh the importance of each neighbor accordingly. We achieve
state-of-the-art results on clustering and image retrieval on the CUB-200-2011,
Cars196, Stanford Online Products, and In-Shop Clothes datasets. To facilitate
further research, we make available the code and the models at
https://github.com/dvl-tum/intra_batch_connections.