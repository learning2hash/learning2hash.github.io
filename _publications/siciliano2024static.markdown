---
layout: publication
title: Static Pruning In Dense Retrieval Using Matrix Decomposition
authors: Federico Siciliano, Francesca Pezzuti, Nicola Tonellotto, Fabrizio Silvestri
conference: Arxiv
year: 2024
bibkey: siciliano2024static
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.09983'}]
tags: ["Efficiency"]
short_authors: Siciliano et al.
---
In the era of dense retrieval, document indexing and retrieval is largely
based on encoding models that transform text documents into embeddings. The
efficiency of retrieval is directly proportional to the number of documents and
the size of the embeddings. Recent studies have shown that it is possible to
reduce embedding size without sacrificing - and in some cases improving - the
retrieval effectiveness. However, the methods introduced by these studies are
query-dependent, so they can't be applied offline and require additional
computations during query processing, thus negatively impacting the retrieval
efficiency. In this paper, we present a novel static pruning method for
reducing the dimensionality of embeddings using Principal Components Analysis.
This approach is query-independent and can be executed offline, leading to a
significant boost in dense retrieval efficiency with a negligible impact on the
system effectiveness. Our experiments show that our proposed method reduces the
dimensionality of document representations by over 50% with up to a 5%
reduction in NDCG@10, for different dense retrieval models.