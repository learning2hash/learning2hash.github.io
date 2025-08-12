---
layout: publication
title: 'Parallel Integer Sort: Theory And Practice'
authors: Xiaojun Dong, Laxman Dhulipala, Yan Gu, Yihan Sun
conference: Proceedings of the 29th ACM SIGPLAN Annual Symposium on Principles and
  Practice of Parallel Programming
year: 2024
bibkey: dong2024parallel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.00710'}]
tags: []
short_authors: Dong et al.
---
Integer sorting is a fundamental problem in computer science. This paper
studies parallel integer sort both in theory and in practice. In theory, we
show tighter bounds for a class of existing practical integer sort algorithms,
which provides a solid theoretical foundation for their widespread usage in
practice and strong performance. In practice, we design a new integer sorting
algorithm, \textsf\{DovetailSort\}, that is theoretically-efficient and has good
practical performance.
  In particular, \textsf\{DovetailSort\} overcomes a common challenge in existing
parallel integer sorting algorithms, which is the difficulty of detecting and
taking advantage of duplicate keys. The key insight in \textsf\{DovetailSort\} is
to combine algorithmic ideas from both integer- and comparison-sorting
algorithms. In our experiments, \textsf\{DovetailSort\} achieves competitive or
better performance than existing state-of-the-art parallel integer and
comparison sorting algorithms on various synthetic and real-world datasets.