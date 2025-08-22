---
layout: publication
title: 'Wl-align: Weisfeiler-lehman Relabeling For Aligning Users Across Networks
  Via Regularized Representation Learning'
authors: Li Liu, Penggang Chen, Xin Li, William K. Cheung, Youmin Zhang, Qun Liu,
  Guoyin Wang
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2023
bibkey: liu2022wl
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.14182'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Tools & Libraries"]
short_authors: Liu et al.
---
Aligning users across networks using graph representation learning has been
found effective where the alignment is accomplished in a low-dimensional
embedding space. Yet, achieving highly precise alignment is still challenging,
especially when nodes with long-range connectivity to the labeled anchors are
encountered. To alleviate this limitation, we purposefully designed WL-Align
which adopts a regularized representation learning framework to learn
distinctive node representations. It extends the Weisfeiler-Lehman Isormorphism
Test and learns the alignment in alternating phases of "across-network
Weisfeiler-Lehman relabeling" and "proximity-preserving representation
learning". The across-network Weisfeiler-Lehman relabeling is achieved through
iterating the anchor-based label propagation and a similarity-based hashing to
exploit the known anchors' connectivity to different nodes in an efficient and
robust manner. The representation learning module preserves the second-order
proximity within individual networks and is regularized by the across-network
Weisfeiler-Lehman hash labels. Extensive experiments on real-world and
synthetic datasets have demonstrated that our proposed WL-Align outperforms the
state-of-the-art methods, achieving significant performance improvements in the
"exact matching" scenario. Data and code of WL-Align are available at
https://github.com/ChenPengGang/WLAlignCode.