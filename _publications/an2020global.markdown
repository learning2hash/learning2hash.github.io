---
layout: publication
title: Global Image Sentiment Transfer
authors: Jie An, Tianlang Chen, Songyang Zhang, Jiebo Luo
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: an2020global
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11989'}]
tags: ["Image Retrieval"]
short_authors: An et al.
---
Transferring the sentiment of an image is an unexplored research topic in the
area of computer vision. This work proposes a novel framework consisting of a
reference image retrieval step and a global sentiment transfer step to transfer
sentiments of images according to a given sentiment tag. The proposed image
retrieval algorithm is based on the SSIM index. The retrieved reference images
by the proposed algorithm are more content-related against the algorithm based
on the perceptual loss. Therefore can lead to a better image sentiment transfer
result. In addition, we propose a global sentiment transfer step, which employs
an optimization algorithm to iteratively transfer sentiment of images based on
feature maps produced by the Densenet121 architecture. The proposed sentiment
transfer algorithm can transfer the sentiment of images while ensuring the
content structure of the input image intact. The qualitative and quantitative
experiments demonstrate that the proposed sentiment transfer framework
outperforms existing artistic and photorealistic style transfer algorithms in
making reliable sentiment transfer results with rich and exact details.