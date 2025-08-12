---
layout: publication
title: 'Instantembedding: Efficient Local Node Representations'
authors: "\u015Etefan Post\u0103varu, Anton Tsitsulin, Filipe Miguel Gon\xE7alves\
  \ de Almeida, Yingtao Tian, Silvio Lattanzi, Bryan Perozzi"
conference: Arxiv
year: 2020
bibkey: "post\u0103varu2020instantembedding"
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.06992'}]
tags: ["Unsupervised"]
short_authors: "Post\u0103varu et al."
---
In this paper, we introduce InstantEmbedding, an efficient method for
generating single-node representations using local PageRank computations. We
theoretically prove that our approach produces globally consistent
representations in sublinear time. We demonstrate this empirically by
conducting extensive experiments on real-world datasets with over a billion
edges. Our experiments confirm that InstantEmbedding requires drastically less
computation time (over 9,000 times faster) and less memory (by over 8,000
times) to produce a single node's embedding than traditional methods including
DeepWalk, node2vec, VERSE, and FastRP. We also show that our method produces
high quality representations, demonstrating results that meet or exceed the
state of the art for unsupervised representation learning on tasks like node
classification and link prediction.