---
layout: publication
title: Discretely Coding Semantic Rank Orders For Supervised Image Hashing
authors: Liu Li, Shao, Shen, Yu
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: liu2017discretely
citations: 49
additional_links: [{name: Paper, url: 'https://openaccess.thecvf.com/content_cvpr_2017/papers/Liu_Discretely_Coding_Semantic_CVPR_2017_paper.pdf'}]
tags: ["CVPR", "Compact Codes", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Scalability", "Supervised"]
short_authors: Liu et al.
---
Learning to hash has been recognized to accomplish highly efficient storage and retrieval for large-scale visual data. Particularly, ranking-based hashing techniques have recently attracted broad research attention because ranking accuracy among the retrieved data is well explored and their objective is more applicable to realistic search tasks. However, directly optimizing discrete hash codes without continuous-relaxations on a nonlinear ranking objective is infeasible by either traditional optimization methods or even recent discrete hashing algorithms. To address this challenging issue, in this paper, we introduce a novel supervised hashing method, dubbed Discrete Semantic Ranking Hashing (DSeRH), which aims to directly embed semantic rank orders into binary codes. In DSeRH, a generalized Adaptive Discrete Minimization (ADM) approach is proposed to discretely optimize binary codes with the quadratic nonlinear ranking objective in an iterative manner and is guaranteed to converge quickly. Additionally, instead of using 0/1 independent labels to form rank orders as in previous works, we generate the listwise rank orders from the high-level semantic word embeddings which can quantitatively capture the intrinsic correlation between different categories. We evaluate our DSeRH, coupled with both linear and deep convolutional neural network (CNN) hash functions, on three image datasets, i.e., CIFAR-10, SUN397 and ImageNet100, and the results manifest that DSeRH can outperform the state-of-the-art ranking-based hashing methods.