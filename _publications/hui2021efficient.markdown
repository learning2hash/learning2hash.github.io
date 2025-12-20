---
layout: publication
title: Efficient 3D Point Cloud Feature Learning For Large-scale Place Recognition
authors: Le Hui, Mingmei Cheng, Jin Xie, Jian Yang
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: hui2021efficient
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.02374'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Neural Hashing", "Scalability"]
short_authors: Hui et al.
---
Point cloud based retrieval for place recognition is still a challenging
problem due to drastic appearance and illumination changes of scenes in
changing environments. Existing deep learning based global descriptors for the
retrieval task usually consume a large amount of computation resources (e.g.,
memory), which may not be suitable for the cases of limited hardware resources.
In this paper, we develop an efficient point cloud learning network (EPC-Net)
to form a global descriptor for visual place recognition, which can obtain good
performance and reduce computation memory and inference time. First, we propose
a lightweight but effective neural network module, called ProxyConv, to
aggregate the local geometric features of point clouds. We leverage the spatial
adjacent matrix and proxy points to simplify the original edge convolution for
lower memory consumption. Then, we design a lightweight grouped VLAD network
(G-VLAD) to form global descriptors for retrieval. Compared with the original
VLAD network, we propose a grouped fully connected (GFC) layer to decompose the
high-dimensional vectors into a group of low-dimensional vectors, which can
reduce the number of parameters of the network and maintain the discrimination
of the feature vector. Finally, to further reduce the inference time, we
develop a simple version of EPC-Net, called EPC-Net-L, which consists of two
ProxyConv modules and one max pooling layer to aggregate global descriptors. By
distilling the knowledge from EPC-Net, EPC-Net-L can obtain discriminative
global descriptors for retrieval. Extensive experiments on the Oxford dataset
and three in-house datasets demonstrate that our proposed method can achieve
state-of-the-art performance with lower parameters, FLOPs, and runtime per
frame.