---
layout: publication
title: Locally-adaptive Quantization For Streaming Vector Search
authors: Aguerrebere Cecilia, Hildebrand Mark, Bhati Ishwar Singh, Willke Theodore, Tepper Mariano
conference: "Arxiv"
year: 2024
bibkey: aguerrebere2024locally
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2402.02044"}
tags: ['ARXIV', 'Quantisation']
---
<p>Retrieving the most similar vector embeddings to a given query among
a massive collection of vectors has long been a key component of
countless real-world applications. The recently introduced
Retrieval-Augmented Generation is one of the most prominent examples.
For many of these applications, the database evolves over time by
inserting new data and removing outdated data. In these cases, the
retrieval problem is known as streaming similarity search. While
Locally-Adaptive Vector Quantization (LVQ), a highly efficient vector
compression method, yields state-of-the-art search performance for
non-evolving databases, its usefulness in the streaming setting has not
been yet established. In this work, we study LVQ in streaming similarity
search. In support of our evaluation, we introduce two improvements of
LVQ: Turbo LVQ and multi-means LVQ that boost its search performance by
up to 28% and 27%, respectively. Our studies show that LVQ and its new
variants enable blazing fast vector search, outperforming its closest
competitor by up to 9.4x for identically distributed data and by up to
8.8x under the challenging scenario of data distribution shifts (i.e.,
where the statistical distribution of the data changes over time). We
release our contributions as part of Scalable Vector Search, an
open-source library for high-performance similarity search.</p>
