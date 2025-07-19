---
layout: publication
title: Iterative Manifold Embedding Layer Learned By Incomplete Data For Large-scale
  Image Retrieval
authors: Xu et al.
conference: IEEE Transactions on Multimedia
year: 2018
bibkey: xu2018iterative
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.09862'}]
tags: [Image Retrieval, SCALABILITY]
---
Existing manifold learning methods are not appropriate for image retrieval
task, because most of them are unable to process query image and they have much
additional computational cost especially for large scale database. Therefore,
we propose the iterative manifold embedding (IME) layer, of which the weights
are learned off-line by unsupervised strategy, to explore the intrinsic
manifolds by incomplete data. On the large scale database that contains 27000
images, IME layer is more than 120 times faster than other manifold learning
methods to embed the original representations at query time. We embed the
original descriptors of database images which lie on manifold in a high
dimensional space into manifold-based representations iteratively to generate
the IME representations in off-line learning stage. According to the original
descriptors and the IME representations of database images, we estimate the
weights of IME layer by ridge regression. In on-line retrieval stage, we employ
the IME layer to map the original representation of query image with ignorable
time cost (2 milliseconds). We experiment on five public standard datasets for
image retrieval. The proposed IME layer significantly outperforms related
dimension reduction methods and manifold learning methods. Without
post-processing, Our IME layer achieves a boost in performance of
state-of-the-art image retrieval methods with post-processing on most datasets,
and needs less computational cost.