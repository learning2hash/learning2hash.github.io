---
layout: publication
title: Generative Multi-hop Retrieval
authors: Hyunji Lee, Sohee Yang, Hanseok Oh, Minjoon Seo
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: lee2022generative
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.13596'}]
tags: [EMNLP, Evaluation, Datasets, Text Retrieval]
short_authors: Lee et al.
---
A common practice for text retrieval is to use an encoder to map the
documents and the query to a common vector space and perform a nearest neighbor
search (NNS); multi-hop retrieval also often adopts the same paradigm, usually
with a modification of iteratively reformulating the query vector so that it
can retrieve different documents at each hop. However, such a bi-encoder
approach has limitations in multi-hop settings; (1) the reformulated query gets
longer as the number of hops increases, which further tightens the embedding
bottleneck of the query vector, and (2) it is prone to error propagation. In
this paper, we focus on alleviating these limitations in multi-hop settings by
formulating the problem in a fully generative way. We propose an
encoder-decoder model that performs multi-hop retrieval by simply generating
the entire text sequences of the retrieval targets, which means the query and
the documents interact in the language model's parametric space rather than L2
or inner product space as in the bi-encoder approach. Our approach, Generative
Multi-hop Retrieval(GMR), consistently achieves comparable or higher
performance than bi-encoder models in five datasets while demonstrating
superior GPU memory and storage footprint.