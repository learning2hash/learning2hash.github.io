---
layout: publication
title: Leveraging Local And Global Descriptors In Parallel To Search Correspondences
  For Visual Localization
authors: Pengju Zhang, Yihong Wu, Bingxi Liu
conference: Pattern Recognition
year: 2021
bibkey: zhang2020leveraging
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.10891'}]
tags: ["Image Retrieval"]
short_authors: Pengju Zhang, Yihong Wu, Bingxi Liu
---
Visual localization to compute 6DoF camera pose from a given image has wide
applications such as in robotics, virtual reality, augmented reality, etc. Two
kinds of descriptors are important for the visual localization. One is global
descriptors that extract the whole feature from each image. The other is local
descriptors that extract the local feature from each image patch usually
enclosing a key point. More and more methods of the visual localization have
two stages: at first to perform image retrieval by global descriptors and then
from the retrieval feedback to make 2D-3D point correspondences by local
descriptors. The two stages are in serial for most of the methods. This simple
combination has not achieved superiority of fusing local and global
descriptors. The 3D points obtained from the retrieval feedback are as the
nearest neighbor candidates of the 2D image points only by global descriptors.
Each of the 2D image points is also called a query local feature when
performing the 2D-3D point correspondences. In this paper, we propose a novel
parallel search framework, which leverages advantages of both local and global
descriptors to get nearest neighbor candidates of a query local feature.
Specifically, besides using deep learning based global descriptors, we also
utilize local descriptors to construct random tree structures for obtaining
nearest neighbor candidates of the query local feature. We propose a new
probabilistic model and a new deep learning based local descriptor when
constructing the random trees. A weighted Hamming regularization term to keep
discriminativeness after binarization is given in the loss function for the
proposed local descriptor. The loss function co-trains both real and binary
descriptors of which the results are integrated into the random trees.