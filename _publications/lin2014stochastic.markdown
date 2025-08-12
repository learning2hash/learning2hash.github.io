---
layout: publication
title: Stochastic Coordinate Coding And Its Application For Drosophila Gene Expression
  Pattern Annotation
authors: Binbin Lin, Qingyang Li, Qian Sun, Ming-Jun Lai, Ian Davidson, Wei Fan, Jieping
  Ye
conference: Arxiv
year: 2014
bibkey: lin2014stochastic
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.8147'}]
tags: []
short_authors: Lin et al.
---
\textit\{Drosophila melanogaster\} has been established as a model organism for
investigating the fundamental principles of developmental gene interactions.
The gene expression patterns of \textit\{Drosophila melanogaster\} can be
documented as digital images, which are annotated with anatomical ontology
terms to facilitate pattern discovery and comparison. The automated annotation
of gene expression pattern images has received increasing attention due to the
recent expansion of the image database. The effectiveness of gene expression
pattern annotation relies on the quality of feature representation. Previous
studies have demonstrated that sparse coding is effective for extracting
features from gene expression images. However, solving sparse coding remains a
computationally challenging problem, especially when dealing with large-scale
data sets and learning large size dictionaries. In this paper, we propose a
novel algorithm to solve the sparse coding problem, called Stochastic
Coordinate Coding (SCC). The proposed algorithm alternatively updates the
sparse codes via just a few steps of coordinate descent and updates the
dictionary via second order stochastic gradient descent. The computational cost
is further reduced by focusing on the non-zero components of the sparse codes
and the corresponding columns of the dictionary only in the updating procedure.
Thus, the proposed algorithm significantly improves the efficiency and the
scalability, making sparse coding applicable for large-scale data sets and
large dictionary sizes. Our experiments on Drosophila gene expression data sets
demonstrate the efficiency and the effectiveness of the proposed algorithm.