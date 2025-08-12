---
layout: publication
title: Towards A Flexible Embedding Learning Framework
authors: Chin-Chia Michael Yeh, Dhruv Gelda, Zhongfang Zhuang, Yan Zheng, Liang Gou,
  Wei Zhang
conference: Arxiv
year: 2020
bibkey: yeh2020towards
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.10989'}]
tags: []
short_authors: Yeh et al.
---
Representation learning is a fundamental building block for analyzing
entities in a database. While the existing embedding learning methods are
effective in various data mining problems, their applicability is often limited
because these methods have pre-determined assumptions on the type of semantics
captured by the learned embeddings, and the assumptions may not well align with
specific downstream tasks. In this work, we propose an embedding learning
framework that 1) uses an input format that is agnostic to input data type, 2)
is flexible in terms of the relationships that can be embedded into the learned
representations, and 3) provides an intuitive pathway to incorporate domain
knowledge into the embedding learning process. Our proposed framework utilizes
a set of entity-relation-matrices as the input, which quantifies the affinities
among different entities in the database. Moreover, a sampling mechanism is
carefully designed to establish a direct connection between the input and the
information captured by the output embeddings. To complete the representation
learning toolbox, we also outline a simple yet effective post-processing
technique to properly visualize the learned embeddings. Our empirical results
demonstrate that the proposed framework, in conjunction with a set of relevant
entity-relation-matrices, outperforms the existing state-of-the-art approaches
in various data mining tasks.