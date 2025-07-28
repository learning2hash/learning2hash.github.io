---
layout: publication
title: Large-scale Visual Search With Binary Distributed Graph At Alibaba
authors: Kang Zhao, Pan Pan, Yun Zheng, Yanhao Zhang, Changxu Wang, Yingya Zhang,
  Yinghui Xu, Rong Jin
conference: Proceedings of the 28th ACM International Conference on Information and
  Knowledge Management
year: 2019
bibkey: zhao2019large
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04656'}]
tags: ["CIKM", "Image Retrieval"]
short_authors: Zhao et al.
---
Graph-based approximate nearest neighbor search has attracted more and more
attentions due to its online search advantages. Numbers of methods studying the
enhancement of speed and recall have been put forward. However, few of them
focus on the efficiency and scale of offline graph-construction. For a deployed
visual search system with several billions of online images in total, building
a billion-scale offline graph in hours is essential, which is almost
unachievable by most existing methods. In this paper, we propose a novel
algorithm called Binary Distributed Graph to solve this problem. Specifically,
we combine binary codes with graph structure to speedup online and offline
procedures, and achieve comparable performance with the ones in real-value
based scenarios by recalling more binary candidates. Furthermore, the
graph-construction is optimized to completely distributed implementation, which
significantly accelerates the offline process and gets rid of the limitation of
memory and disk within a single machine. Experimental comparisons on Alibaba
Commodity Data Set (more than three billion images) show that the proposed
method outperforms the state-of-the-art with respect to the online/offline
trade-off.