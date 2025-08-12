---
layout: publication
title: 'Revised Conditional T-sne: Looking Beyond The Nearest Neighbors'
authors: Edith Heiter, Bo Kang, Ruth Seurinck, Jefrey Lijffijt
conference: Lecture Notes in Computer Science
year: 2023
bibkey: heiter2023revised
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.03493'}]
tags: []
short_authors: Heiter et al.
---
Conditional t-SNE (ct-SNE) is a recent extension to t-SNE that allows removal
of known cluster information from the embedding, to obtain a visualization
revealing structure beyond label information. This is useful, for example, when
one wants to factor out unwanted differences between a set of classes. We show
that ct-SNE fails in many realistic settings, namely if the data is well
clustered over the labels in the original high-dimensional space. We introduce
a revised method by conditioning the high-dimensional similarities instead of
the low-dimensional similarities and storing within- and across-label nearest
neighbors separately. This also enables the use of recently proposed speedups
for t-SNE, improving the scalability. From experiments on synthetic data, we
find that our proposed method resolves the considered problems and improves the
embedding quality. On real data containing batch effects, the expected
improvement is not always there. We argue revised ct-SNE is preferable overall,
given its improved scalability. The results also highlight new open questions,
such as how to handle distance variations between clusters.