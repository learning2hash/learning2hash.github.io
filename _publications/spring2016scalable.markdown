---
layout: publication
title: Scalable And Sustainable Deep Learning Via Randomized Hashing
authors: Spring Ryan, Shrivastava Anshumali
conference: Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge
  Discovery and Data Mining
year: 2017
bibkey: spring2016scalable
citations: 108
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.08194'}]
tags: ["Hashing-Methods", "Efficiency", "Scalability", "Datasets", "KDD"]
short_authors: Spring Ryan, Shrivastava Anshumali
---
Current deep learning architectures are growing larger in order to learn from
complex datasets. These architectures require giant matrix multiplication
operations to train millions of parameters. Conversely, there is another
growing trend to bring deep learning to low-power, embedded devices. The matrix
operations, associated with both training and testing of deep networks, are
very expensive from a computational and energy standpoint. We present a novel
hashing based technique to drastically reduce the amount of computation needed
to train and test deep networks. Our approach combines recent ideas from
adaptive dropouts and randomized hashing for maximum inner product search to
select the nodes with the highest activation efficiently. Our new algorithm for
deep learning reduces the overall computational cost of forward and
back-propagation by operating on significantly fewer (sparse) nodes. As a
consequence, our algorithm uses only 5% of the total multiplications, while
keeping on average within 1% of the accuracy of the original model. A unique
property of the proposed hashing based back-propagation is that the updates are
always sparse. Due to the sparse gradient updates, our algorithm is ideally
suited for asynchronous and parallel training leading to near linear speedup
with increasing number of cores. We demonstrate the scalability and
sustainability (energy efficiency) of our proposed algorithm via rigorous
experimental evaluations on several real datasets.