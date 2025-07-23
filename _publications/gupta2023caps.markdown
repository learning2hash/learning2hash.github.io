---
layout: publication
title: 'CAPS: A Practical Partition Index For Filtered Similarity Search'
authors: Gupta Gaurav, Yi Jonah, Coleman Benjamin, Luo Chen, Lakshman Vihan, Shrivastava
  Anshumali
conference: Arxiv
year: 2023
bibkey: gupta2023caps
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15014'}]
tags: ["Efficiency", "Evaluation", "Graph-based ANN", "Large-Scale Search", "Similarity Search", "Vector Indexing"]
short_authors: Gupta et al.
---
With the surging popularity of approximate near-neighbor search (ANNS),
driven by advances in neural representation learning, the ability to serve
queries accompanied by a set of constraints has become an area of intense
interest. While the community has recently proposed several algorithms for
constrained ANNS, almost all of these methods focus on integration with
graph-based indexes, the predominant class of algorithms achieving
state-of-the-art performance in latency-recall tradeoffs. In this work, we take
a different approach and focus on developing a constrained ANNS algorithm via
space partitioning as opposed to graphs. To that end, we introduce Constrained
Approximate Partitioned Search (CAPS), an index for ANNS with filters via space
partitions that not only retains the benefits of a partition-based algorithm
but also outperforms state-of-the-art graph-based constrained search techniques
in recall-latency tradeoffs, with only 10% of the index size.