---
layout: publication
title: 'CAPS: A Practical Partition Index For Filtered Similarity Search'
authors: Gupta et al.
conference: Proceedings of the 37th international ACM SIGIR conference on Research
  &amp; development in information retrieval
year: 2023
bibkey: gupta2023caps
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15014'}]
tags: ["SIGIR", "Text Retrieval", "Similarity Search"]
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