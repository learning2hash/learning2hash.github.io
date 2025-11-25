---
layout: publication
title: Unconventional Application Of K-means For Distributed Approximate Similarity
  Search
authors: "Felipe Ortega, Maria Jesus Algar, Isaac Mart\xEDn de Diego, Javier M. Moguerza"
conference: Information Sciences
year: 2022
bibkey: ortega2022unconventional
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.02734'}]
tags: ["Similarity Search", "Vector Indexing"]
short_authors: Ortega et al.
---
Similarity search based on a distance function in metric spaces is a
fundamental problem for many applications. Queries for similar objects lead to
the well-known machine learning task of nearest-neighbours identification. Many
data indexing strategies, collectively known as Metric Access Methods (MAM),
have been proposed to speed up queries for similar elements in this context.
Moreover, since exact approaches to solve similarity queries can be complex and
time-consuming, alternative options have appeared to reduce query execution
time, such as returning approximate results or resorting to distributed
computing platforms. In this paper, we introduce MASK (Multilevel Approximate
Similarity search with \(k\)-means), an unconventional application of the
\(k\)-means algorithm as the foundation of a multilevel index structure for
approximate similarity search, suitable for metric spaces. We show that
inherent properties of \(k\)-means, like representing high-density data areas
with fewer prototypes, can be leveraged for this purpose. An implementation of
this new indexing method is evaluated, using a synthetic dataset and a
real-world dataset in a high-dimensional and high-sparsity space. Results are
promising and underpin the applicability of this novel indexing method in
multiple domains.