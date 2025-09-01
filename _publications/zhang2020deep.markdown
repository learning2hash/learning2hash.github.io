---
layout: publication
title: Deep Pairwise Hashing For Cold-start Recommendation
authors: Yan Zhang, Ivor W. Tsang, Hongzhi Yin, Guowu Yang, Defu Lian, Jingjing Li
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: zhang2020deep
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.00944'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Neural Hashing", "Recommender Systems", "Tools & Libraries"]
short_authors: Zhang et al.
---
Recommendation efficiency and data sparsity problems have been regarded as
two challenges of improving performance for online recommendation. Most of the
previous related work focus on improving recommendation accuracy instead of
efficiency. In this paper, we propose a Deep Pairwise Hashing (DPH) to map
users and items to binary vectors in Hamming space, where a user's preference
for an item can be efficiently calculated by Hamming distance, which
significantly improves the efficiency of online recommendation. To alleviate
data sparsity and cold-start problems, the user-item interactive information
and item content information are unified to learn effective representations of
items and users. Specifically, we first pre-train robust item representation
from item content data by a Denoising Auto-encoder instead of other
deterministic deep learning frameworks; then we finetune the entire framework
by adding a pairwise loss objective with discrete constraints; moreover, DPH
aims to minimize a pairwise ranking loss that is consistent with the ultimate
goal of recommendation. Finally, we adopt the alternating optimization method
to optimize the proposed model with discrete constraints. Extensive experiments
on three different datasets show that DPH can significantly advance the
state-of-the-art frameworks regarding data sparsity and item cold-start
recommendation.