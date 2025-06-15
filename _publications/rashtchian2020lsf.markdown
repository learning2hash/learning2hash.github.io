---
layout: publication
title: 'Lsf-join: Locality Sensitive Filtering For Distributed All-pairs Set Similarity Under Skew'
authors: Cyrus Rashtchian, Aneesh Sharma, David P. Woodruff
conference: "Arxiv"
year: 2020
citations: 3
bibkey: rashtchian2020lsf
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2003.02972'}
tags: ['Hashing Methods', 'KDD', 'Approximate Nearest Neighbor Search', 'Tools and Libraries', 'Hashing Fundamentals']
---
All-pairs set similarity is a widely used data mining task, even for large
and high-dimensional datasets. Traditionally, similarity search has focused on
discovering very similar pairs, for which a variety of efficient algorithms are
known. However, recent work highlights the importance of finding pairs of sets
with relatively small intersection sizes. For example, in a recommender system,
two users may be alike even though their interests only overlap on a small
percentage of items. In such systems, some dimensions are often highly skewed
because they are very popular. Together these two properties render previous
approaches infeasible for large input sizes. To address this problem, we
present a new distributed algorithm, LSF-Join, for approximate all-pairs set
similarity. The core of our algorithm is a randomized selection procedure based
on Locality Sensitive Filtering. Our method deviates from prior approximate
algorithms, which are based on Locality Sensitive Hashing. Theoretically, we
show that LSF-Join efficiently finds most close pairs, even for small
similarity thresholds and for skewed input sets. We prove guarantees on the
communication, work, and maximum load of LSF-Join, and we also experimentally
demonstrate its accuracy on multiple graphs.
