---
layout: publication
title: Dynamic Superblock Pruning For Fast Learned Sparse Retrieval
authors: Parker Carlson, Wentai Xie, Shanxiu He, Tao Yang
conference: Proceedings of the 48th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2025
bibkey: carlson2025dynamic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.17045'}]
tags: ["Efficiency", "Large Scale Search", "SIGIR", "Text Retrieval"]
short_authors: Carlson et al.
---
This paper proposes superblock pruning (SP) during top-k online document
retrieval for learned sparse representations. SP structures the sparse index as
a set of superblocks on a sequence of document blocks and conducts a
superblock-level selection to decide if some superblocks can be pruned before
visiting their child blocks. SP generalizes the previous flat block or
cluster-based pruning, allowing the early detection of groups of documents that
cannot or are less likely to appear in the final top-k list. SP can accelerate
sparse retrieval in a rank-safe or approximate manner under a high-relevance
competitiveness constraint. Our experiments show that the proposed scheme
significantly outperforms state-of-the-art baselines on MS MARCO passages on a
single-threaded CPU.