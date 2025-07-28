---
layout: publication
title: 'UNIFY: Unified Index For Range Filtered Approximate Nearest Neighbors Search'
authors: Anqi Liang, Pengcheng Zhang, Bin Yao, Zhongpu Chen, Yitong Song, Guangxu
  Cheng
conference: Proceedings of the VLDB Endowment
year: 2024
bibkey: liang2024unify
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.02448'}]
tags: []
short_authors: Liang et al.
---
This paper presents an efficient and scalable framework for Range Filtered Approximate Nearest Neighbors Search (RF-ANNS) over high-dimensional vectors associated with attribute values. Given a query vector \\(q\\) and a range \\([l, h]\\), RF-ANNS aims to find the approximate \\(k\\) nearest neighbors of \\(q\\) among data whose attribute values fall within \\([l, h]\\). Existing methods including pre-, post-, and hybrid filtering strategies that perform attribute range filtering before, after, or during the ANNS process, all suffer from significant performance degradation when query ranges shift. Though building dedicated indexes for each strategy and selecting the best one based on the query range can address this problem, it leads to index consistency and maintenance issues.
  Our framework, called UNIFY, constructs a unified Proximity Graph-based (PG-based) index that seamlessly supports all three strategies. In UNIFY, we introduce SIG, a novel Segmented Inclusive Graph, which segments the dataset by attribute values. It ensures the PG of objects from any segment combinations is a sub-graph of SIG, thereby enabling efficient hybrid filtering by reconstructing and searching a PG from relevant segments. Moreover, we present Hierarchical Segmented Inclusive Graph (HSIG), a variant of SIG which incorporates a hierarchical structure inspired by HNSW to achieve logarithmic hybrid filtering complexity. We also implement pre- and post-filtering for HSIG by fusing skip list connections and compressed HNSW edges into the hierarchical graph. Experimental results show that UNIFY delivers state-of-the-art RF-ANNS performance across small, mid, and large query ranges.