---
layout: publication
title: Co-salient Object Detection With Co-representation Purification
authors: Ziyue Zhu, Zhao Zhang, Zheng Lin, Xing Sun, Ming-Ming Cheng
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: zhu2023co
citations: 23
additional_links: [{name: Code, url: 'https://github.com/ZZY816/CoRP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.07670'}]
tags: []
short_authors: Zhu et al.
---
Co-salient object detection (Co-SOD) aims at discovering the common objects
in a group of relevant images. Mining a co-representation is essential for
locating co-salient objects. Unfortunately, the current Co-SOD method does not
pay enough attention that the information not related to the co-salient object
is included in the co-representation. Such irrelevant information in the
co-representation interferes with its locating of co-salient objects. In this
paper, we propose a Co-Representation Purification (CoRP) method aiming at
searching noise-free co-representation. We search a few pixel-wise embeddings
probably belonging to co-salient regions. These embeddings constitute our
co-representation and guide our prediction. For obtaining purer
co-representation, we use the prediction to iteratively reduce irrelevant
embeddings in our co-representation. Experiments on three datasets demonstrate
that our CoRP achieves state-of-the-art performances on the benchmark datasets.
Our source code is available at https://github.com/ZZY816/CoRP.