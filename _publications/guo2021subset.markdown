---
layout: publication
title: Subset Node Representation Learning Over Large Dynamic Graphs
authors: Xingzhi Guo, Baojian Zhou, Steven Skiena
conference: Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery &amp;
  Data Mining
year: 2021
bibkey: guo2021subset
citations: 13
additional_links: [{name: Code, url: 'https://en.wikipedia.org/wiki/COVID-19_pandemic'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.01570'}]
tags: ["Efficiency", "Evaluation", "Graph Based ANN", "KDD", "Scalability"]
short_authors: Xingzhi Guo, Baojian Zhou, Steven Skiena
---
Dynamic graph representation learning is a task to learn node embeddings over
dynamic networks, and has many important applications, including knowledge
graphs, citation networks to social networks. Graphs of this type are usually
large-scale but only a small subset of vertices are related in downstream
tasks. Current methods are too expensive to this setting as the complexity is
at best linear-dependent on both the number of nodes and edges. In this paper,
we propose a new method, namely Dynamic Personalized PageRank Embedding
(\textsc\{DynamicPPE\}) for learning a target subset of node representations over
large-scale dynamic networks. Based on recent advances in local node embedding
and a novel computation of dynamic personalized PageRank vector (PPV),
\textsc\{DynamicPPE\} has two key ingredients: 1) the per-PPV complexity is
\(\mathcal\{O\}(m \bar\{d\} / \epsilon)\) where \(m,\bar\{d\}\), and \(\epsilon\) are the
number of edges received, average degree, global precision error respectively.
Thus, the per-edge event update of a single node is only dependent on \(\bar\{d\}\)
in average; and 2) by using these high quality PPVs and hash kernels, the
learned embeddings have properties of both locality and global consistency.
These two make it possible to capture the evolution of graph structure
effectively. Experimental results demonstrate both the effectiveness and
efficiency of the proposed method over large-scale dynamic networks. We apply
\textsc\{DynamicPPE\} to capture the embedding change of Chinese cities in the
Wikipedia graph during this ongoing COVID-19 pandemic
(https://en.wikipedia.org/wiki/COVID-19_pandemic). Our results show that these
representations successfully encode the dynamics of the Wikipedia graph.