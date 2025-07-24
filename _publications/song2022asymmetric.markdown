---
layout: publication
title: Asymmetric Hash Code Learning For Remote Sensing Image Retrieval
authors: "Weiwei Song, Zhi Gao, Renwei Dian, Pedram Ghamisi, Yongjun Zhang, J\xF3\
  n Atli Benediktsson"
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2022
bibkey: song2022asymmetric
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.05772'}]
tags: ["Compact Codes", "Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Scalability", "Supervised"]
short_authors: Song et al.
---
Remote sensing image retrieval (RSIR), aiming at searching for a set of
similar items to a given query image, is a very important task in remote
sensing applications. Deep hashing learning as the current mainstream method
has achieved satisfactory retrieval performance. On one hand, various deep
neural networks are used to extract semantic features of remote sensing images.
On the other hand, the hashing techniques are subsequently adopted to map the
high-dimensional deep features to the low-dimensional binary codes. This kind
of methods attempts to learn one hash function for both the query and database
samples in a symmetric way. However, with the number of database samples
increasing, it is typically time-consuming to generate the hash codes of
large-scale database images. In this paper, we propose a novel deep hashing
method, named asymmetric hash code learning (AHCL), for RSIR. The proposed AHCL
generates the hash codes of query and database images in an asymmetric way. In
more detail, the hash codes of query images are obtained by binarizing the
output of the network, while the hash codes of database images are directly
learned by solving the designed objective function. In addition, we combine the
semantic information of each image and the similarity information of pairs of
images as supervised information to train a deep hashing network, which
improves the representation ability of deep features and hash codes. The
experimental results on three public datasets demonstrate that the proposed
method outperforms symmetric methods in terms of retrieval accuracy and
efficiency. The source code is available at
https://github.com/weiweisong415/Demo AHCL for TGRS2022.