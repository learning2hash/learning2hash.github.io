---
layout: publication
title: Deep Heterogeneous Hashing For Face Video Retrieval
authors: Shishi Qiao, Ruiping Wang, Shiguang Shan, Xilin Chen
conference: IEEE Transactions on Image Processing
year: 2019
bibkey: qiao2019deep
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.01048'}]
tags: [Compact Codes, Hashing Methods, Datasets, Video Retrieval, Evaluation, Tools
    & Libraries]
short_authors: Qiao et al.
---
Retrieving videos of a particular person with face image as a query via
hashing technique has many important applications. While face images are
typically represented as vectors in Euclidean space, characterizing face videos
with some robust set modeling techniques (e.g. covariance matrices as exploited
in this study, which reside on Riemannian manifold), has recently shown
appealing advantages. This hence results in a thorny heterogeneous spaces
matching problem. Moreover, hashing with handcrafted features as done in many
existing works is clearly inadequate to achieve desirable performance for this
task. To address such problems, we present an end-to-end Deep Heterogeneous
Hashing (DHH) method that integrates three stages including image feature
learning, video modeling, and heterogeneous hashing in a single framework, to
learn unified binary codes for both face images and videos. To tackle the key
challenge of hashing on the manifold, a well-studied Riemannian kernel mapping
is employed to project data (i.e. covariance matrices) into Euclidean space and
thus enables to embed the two heterogeneous representations into a common
Hamming space, where both intra-space discriminability and inter-space
compatibility are considered. To perform network optimization, the gradient of
the kernel mapping is innovatively derived via structured matrix
backpropagation in a theoretically principled way. Experiments on three
challenging datasets show that our method achieves quite competitive
performance compared with existing hashing methods.