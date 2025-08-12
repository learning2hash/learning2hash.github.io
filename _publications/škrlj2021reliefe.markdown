---
layout: publication
title: 'Reliefe: Feature Ranking In High-dimensional Spaces Via Manifold Embeddings'
authors: "Bla\u017E \u0160krlj, Sa\u0161o D\u017Eeroski, Nada Lavra\u010D, Matej Petkovi\u0107"
conference: Machine Learning
year: 2021
bibkey: "\u0161krlj2021reliefe"
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.09577'}]
tags: []
short_authors: "\u0160krlj et al."
---
Feature ranking has been widely adopted in machine learning applications such
as high-throughput biology and social sciences. The approaches of the popular
Relief family of algorithms assign importances to features by iteratively
accounting for nearest relevant and irrelevant instances. Despite their high
utility, these algorithms can be computationally expensive and not-well suited
for high-dimensional sparse input spaces. In contrast, recent embedding-based
methods learn compact, low-dimensional representations, potentially
facilitating down-stream learning capabilities of conventional learners. This
paper explores how the Relief branch of algorithms can be adapted to benefit
from (Riemannian) manifold-based embeddings of instance and target spaces,
where a given embedding's dimensionality is intrinsic to the dimensionality of
the considered data set. The developed ReliefE algorithm is faster and can
result in better feature rankings, as shown by our evaluation on 20 real-life
data sets for multi-class and multi-label classification tasks. The utility of
ReliefE for high-dimensional data sets is ensured by its implementation that
utilizes sparse matrix algebraic operations. Finally, the relation of ReliefE
to other ranking algorithms is studied via the Fuzzy Jaccard Index.