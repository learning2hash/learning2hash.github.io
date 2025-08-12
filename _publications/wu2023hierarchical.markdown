---
layout: publication
title: Hierarchical And Contrastive Representation Learning For Knowledge-aware Recommendation
authors: Bingchao Wu, Yangyuxuan Kang, Daoguang Zan, Bei Guan, Yongji Wang
conference: 2023 IEEE International Conference on Multimedia and Expo (ICME)
year: 2023
bibkey: wu2023hierarchical
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.07506'}]
tags: ["Recommender Systems", "Self-Supervised"]
short_authors: Wu et al.
---
Incorporating knowledge graph into recommendation is an effective way to
alleviate data sparsity. Most existing knowledge-aware methods usually perform
recursive embedding propagation by enumerating graph neighbors. However, the
number of nodes' neighbors grows exponentially as the hop number increases,
forcing the nodes to be aware of vast neighbors under this recursive
propagation for distilling the high-order semantic relatedness. This may induce
more harmful noise than useful information into recommendation, leading the
learned node representations to be indistinguishable from each other, that is,
the well-known over-smoothing issue. To relieve this issue, we propose a
Hierarchical and CONtrastive representation learning framework for
knowledge-aware recommendation named HiCON. Specifically, for avoiding the
exponential expansion of neighbors, we propose a hierarchical message
aggregation mechanism to interact separately with low-order neighbors and
meta-path-constrained high-order neighbors. Moreover, we also perform
cross-order contrastive learning to enforce the representations to be more
discriminative. Extensive experiments on three datasets show the remarkable
superiority of HiCON over state-of-the-art approaches.