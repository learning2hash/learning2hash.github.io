---
layout: publication
title: Supervised Online Hashing Via Hadamard Codebook Learning
authors: Mingbao Lin, Rongrong Ji, Hong Liu, Yongjian Liu
conference: Proceedings of the 26th ACM international conference on Multimedia
year: 2018
bibkey: lin2018supervised
citations: 64
additional_links: [{name: Code, url: 'https://github.com/lmbxmu/mycode/tree/master/2018ACMMM_HCOH.'},
  {name: Paper, url: 'https://arxiv.org/abs/1905.03694'}]
tags: [Scalability, Datasets, Supervised, Hashing Methods, Locality Sensitive Hashing,
  Compact Codes, Robustness, Evaluation]
short_authors: Lin et al.
---
In recent years, binary code learning, a.k.a hashing, has received extensive
attention in large-scale multimedia retrieval. It aims to encode
high-dimensional data points to binary codes, hence the original
high-dimensional metric space can be efficiently approximated via Hamming
space. However, most existing hashing methods adopted offline batch learning,
which is not suitable to handle incremental datasets with streaming data or new
instances. In contrast, the robustness of the existing online hashing remains
as an open problem, while the embedding of supervised/semantic information
hardly boosts the performance of the online hashing, mainly due to the defect
of unknown category numbers in supervised learning. In this paper, we proposed
an online hashing scheme, termed Hadamard Codebook based Online Hashing (HCOH),
which aims to solve the above problems towards robust and supervised online
hashing. In particular, we first assign an appropriate high-dimensional binary
codes to each class label, which is generated randomly by Hadamard codes to
each class label, which is generated randomly by Hadamard codes. Subsequently,
LSH is adopted to reduce the length of such Hadamard codes in accordance with
the hash bits, which can adapt the predefined binary codes online, and
theoretically guarantee the semantic similarity. Finally, we consider the
setting of stochastic data acquisition, which facilitates our method to
efficiently learn the corresponding hashing functions via stochastic gradient
descend (SGD) online. Notably, the proposed HCOH can be embedded with
supervised labels and it not limited to a predefined category number. Extensive
experiments on three widely-used benchmarks demonstrate the merits of the
proposed scheme over the state-of-the-art methods. The code is available at
https://github.com/lmbxmu/mycode/tree/master/2018ACMMM_HCOH.