---
layout: publication
title: Unsupervised Features Extraction For Binary Similarity Using Graph Embedding
  Neural Networks
authors: Roberto Baldoni, Giuseppe Antonio di Luna, Luca Massarelli, Fabio Petroni,
  Leonardo Querzoni
conference: Arxiv
year: 2018
bibkey: baldoni2018unsupervised
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09683'}]
tags: ["Evaluation", "Supervised", "Unsupervised"]
short_authors: Baldoni et al.
---
In this paper we consider the binary similarity problem that consists in
determining if two binary functions are similar only considering their compiled
form. This problem is know to be crucial in several application scenarios, such
as copyright disputes, malware analysis, vulnerability detection, etc. The
current state-of-the-art solutions in this field work by creating an embedding
model that maps binary functions into vectors in \(\mathbb\{R\}^\{n\}\). Such
embedding model captures syntactic and semantic similarity between binaries,
i.e., similar binary functions are mapped to points that are close in the
vector space. This strategy has many advantages, one of them is the possibility
to precompute embeddings of several binary functions, and then compare them
with simple geometric operations (e.g., dot product). In [32] functions are
first transformed in Annotated Control Flow Graphs (ACFGs) constituted by
manually engineered features and then graphs are embedded into vectors using a
deep neural network architecture. In this paper we propose and test several
ways to compute annotated control flow graphs that use unsupervised approaches
for feature learning, without incurring a human bias. Our methods are inspired
after techniques used in the natural language processing community (e.g., we
use word2vec to encode assembly instructions). We show that our approach is
indeed successful, and it leads to better performance than previous
state-of-the-art solutions. Furthermore, we report on a qualitative analysis of
functions embeddings. We found interesting cases in which embeddings are
clustered according to the semantic of the original binary function.