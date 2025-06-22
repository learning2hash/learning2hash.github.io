---
layout: publication
title: On The Complexity Of Inner Product Similarity Join
authors: Thomas D. Ahle, Rasmus Pagh, Ilya Razenshteyn, Francesco Silvestri
conference: Arxiv
year: 2015
citations: 22
bibkey: ahle2015complexity
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1510.02824'}]
tags: [Indexing, Hashing Methods, ANN Search]
---
A number of tasks in classification, information retrieval, recommendation
systems, and record linkage reduce to the core problem of inner product
similarity join (IPS join): identifying pairs of vectors in a collection that
have a sufficiently large inner product. IPS join is well understood when
vectors are normalized and some approximation of inner products is allowed.
However, the general case where vectors may have any length appears much more
challenging. Recently, new upper bounds based on asymmetric locality-sensitive
hashing (ALSH) and asymmetric embeddings have emerged, but little has been
known on the lower bound side. In this paper we initiate a systematic study of
inner product similarity join, showing new lower and upper bounds. Our main
results are:
  * Approximation hardness of IPS join in subquadratic time, assuming the
strong exponential time hypothesis.
  * New upper and lower bounds for (A)LSH-based algorithms. In particular, we
show that asymmetry can be avoided by relaxing the LSH definition to only
consider the collision probability of distinct elements.
  * A new indexing method for IPS based on linear sketches, implying that our
hardness results are not far from being tight.
  Our technical contributions include new asymmetric embeddings that may be of
independent interest. At the conceptual level we strive to provide greater
clarity, for example by distinguishing among signed and unsigned variants of
IPS join and shedding new light on the effect of asymmetry.