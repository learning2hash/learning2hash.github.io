---
layout: publication
title: Deep Triplet Quantization
authors: Bin Liu, Yue Cao, Mingsheng Long, Jianmin Wang, Jingdong Wang
conference: Proceedings of the 26th ACM international conference on Multimedia
year: 2018
bibkey: liu2018deep
citations: 105
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.00153'}]
tags: ["Compact Codes", "Datasets", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Quantization", "Similarity Search"]
short_authors: Liu et al.
---
Deep hashing establishes efficient and effective image retrieval by
end-to-end learning of deep representations and hash codes from similarity
data. We present a compact coding solution, focusing on deep learning to
quantization approach that has shown superior performance over hashing
solutions for similarity retrieval. We propose Deep Triplet Quantization (DTQ),
a novel approach to learning deep quantization models from the similarity
triplets. To enable more effective triplet training, we design a new triplet
selection approach, Group Hard, that randomly selects hard triplets in each
image group. To generate compact binary codes, we further apply a triplet
quantization with weak orthogonality during triplet training. The quantization
loss reduces the codebook redundancy and enhances the quantizability of deep
representations through back-propagation. Extensive experiments demonstrate
that DTQ can generate high-quality and compact binary codes, which yields
state-of-the-art image retrieval performance on three benchmark datasets,
NUS-WIDE, CIFAR-10, and MS-COCO.