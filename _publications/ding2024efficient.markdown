---
layout: publication
title: Efficient Retrieval With Learned Similarities
authors: Ding Bailu, Zhai Jiaqi
conference: "Arxiv"
year: 2024
bibkey: ding2024efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2407.15462"}
tags: ['ARXIV', 'Supervised']
---
<p>Retrieval plays a fundamental role in recommendation systems, search,
and natural language processing by efficiently finding relevant items
from a large corpus given a query. Dot products have been widely used as
the similarity function in such retrieval tasks, thanks to Maximum Inner
Product Search (MIPS) that enabled efficient retrieval based on dot
products. However, state-of-the-art retrieval algorithms have migrated
to learned similarities. Such algorithms vary in form; the queries can
be represented with multiple embeddings, complex neural networks can be
deployed, the item ids can be decoded directly from queries using beam
search, and multiple approaches can be combined in hybrid solutions.
Unfortunately, we lack efficient solutions for retrieval in these
state-of-the-art setups. Our work investigates techniques for
approximate nearest neighbor search with learned similarity functions.
We first prove that Mixture-of-Logits (MoL) is a universal approximator,
and can express all learned similarity functions. We next propose
techniques to retrieve the approximate top K results using MoL with a
tight bound. We finally compare our techniques with existing approaches,
showing that MoL sets new state-of-the-art results on recommendation
retrieval tasks, and our approximate top-k retrieval with learned
similarities outperforms baselines by up to two orders of magnitude in
latency, while achieving &gt; .99 recall rate of exact algorithms.</p>
