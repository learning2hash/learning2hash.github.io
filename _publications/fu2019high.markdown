---
layout: publication
title: 'High Dimensional Similarity Search With Satellite System Graph: Efficiency,
  Scalability, And Unindexed Query Compatibility'
authors: Cong Fu, Changxu Wang, Deng Cai
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: fu2019high
citations: 43
additional_links: [{name: Code, url: 'https://github.com/ZJULearning/SSG'}, {name: Paper,
    url: 'https://arxiv.org/abs/1907.06146'}]
tags: [Evaluation, Similarity Search, Efficiency, Graph-based ANN, Scalability]
short_authors: Cong Fu, Changxu Wang, Deng Cai
---
Approximate Nearest Neighbor Search (ANNS) in high dimensional space is
essential in database and information retrieval. Recently, there has been a
surge of interest in exploring efficient graph-based indices for the ANNS
problem. Among them, Navigating Spreading-out Graph (NSG) provides fine
theoretical analysis and achieves state-of-the-art performance. However, we
find there are several limitations with NSG: 1) NSG has no theoretical
guarantee on nearest neighbor search when the query is not indexed in the
database; 2) NSG is too sparse which harms the search performance. In addition,
NSG suffers from high indexing complexity. To address the above problems, we
propose the Satellite System Graphs (SSG) and a practical variant NSSG.
Specifically, we propose a novel pruning strategy to produce SSGs from the
complete graph. SSGs define a new family of MSNETs in which the out-edges of
each node are distributed evenly in all directions. Each node in the graph
builds effective connections to its neighborhood omnidirectionally, whereupon
we derive SSG's excellent theoretical properties for both indexed and unindexed
queries. We can adaptively adjust the sparsity of an SSG with a hyper-parameter
to optimize the search performance. Further, NSSG is proposed to reduce the
indexing complexity of the SSG for large-scale applications. Both theoretical
and extensive experimental analyses are provided to demonstrate the strengths
of the proposed approach over the existing representative algorithms. Our code
has been released at https://github.com/ZJULearning/SSG.