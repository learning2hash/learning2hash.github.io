---
layout: publication
title: 'TPCH: Tensor-interacted Projection And Cooperative Hashing For Multi-view
  Clustering'
authors: Zhongwen Wang, Xingfeng Li, Yinghui Sun, Quansen Sun, Yuan Sun, Han Ling,
  Jian Dai, Zhenwen Ren
conference: Arxiv
year: 2024
bibkey: wang2024tpch
citations: 0
additional_links: [{name: Code, url: 'https://github.com/jankin-wang/TPCH\'}, {name: Paper,
    url: 'https://arxiv.org/abs/2412.18847'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Scalability"]
short_authors: Wang et al.
---
In recent years, anchor and hash-based multi-view clustering methods have
gained attention for their efficiency and simplicity in handling large-scale
data. However, existing methods often overlook the interactions among
multi-view data and higher-order cooperative relationships during projection,
negatively impacting the quality of hash representation in low-dimensional
spaces, clustering performance, and sensitivity to noise. To address this
issue, we propose a novel approach named Tensor-Interacted Projection and
Cooperative Hashing for Multi-View Clustering(TPCH). TPCH stacks multiple
projection matrices into a tensor, taking into account the synergies and
communications during the projection process. By capturing higher-order
multi-view information through dual projection and Hamming space, TPCH employs
an enhanced tensor nuclear norm to learn more compact and distinguishable hash
representations, promoting communication within and between views. Experimental
results demonstrate that this refined method significantly outperforms
state-of-the-art methods in clustering on five large-scale multi-view datasets.
Moreover, in terms of CPU time, TPCH achieves substantial acceleration compared
to the most advanced current methods. The code is available at
\textcolor\{red\}\{https://github.com/jankin-wang/TPCH\}.