---
layout: publication
title: Strongly Constrained Discrete Hashing
authors: Yong Chen, Tian, Zhang, Wang, Zhang
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: chen2020strongly
citations: 50
additional_links: [{name: Paper, url: 'https://doi.org/10.1109/TIP.2020.2963952'}]
tags: ["Compact Codes", "Evaluation", "Hashing Methods", "Image Retrieval", "Quantization", "Scalability", "Supervised"]
short_authors: Chen et al.
---
Learning to hash is a fundamental technique widely used in large-scale image retrieval. Most existing methods for learning to hash address the involved discrete optimization problem by the continuous relaxation of the binary constraint, which usually leads to large quantization errors and consequently suboptimal binary codes. A few discrete hashing methods have emerged recently. However, they either completely ignore some useful constraints (specifically the balance and decorrelation of hash bits) or just turn those constraints into regularizers that would make the optimization easier but less accurate. In this paper, we propose a novel supervised hashing method named Strongly Constrained Discrete Hashing (SCDH) which overcomes such limitations. It can learn the binary codes for all examples in the training set, and meanwhile obtain a hash function for unseen samples with the above mentioned constraints preserved. Although the model of SCDH is fairly sophisticated, we are able to find closed-form solutions to all of its optimization subproblems and thus design an efficient algorithm that converges quickly. In addition, we extend SCDH to a kernelized version SCDH K . Our experiments on three large benchmark datasets have demonstrated that not only can SCDH and SCDH K achieve substantially higher MAP scores than state-of-the-art baselines, but they train much faster than those that are also supervised as well.