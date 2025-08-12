---
layout: publication
title: 'MDR Cluster-debias: A Nonlinear Wordembedding Debiasing Pipeline'
authors: Yuhao Du, Kenneth Joseph
conference: Arxiv
year: 2020
bibkey: du2020mdr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11642'}]
tags: []
short_authors: Yuhao Du, Kenneth Joseph
---
Existing methods for debiasing word embeddings often do so only
superficially, in that words that are stereotypically associated with, e.g., a
particular gender in the original embedding space can still be clustered
together in the debiased space. However, there has yet to be a study that
explores why this residual clustering exists, and how it might be addressed.
The present work fills this gap. We identify two potential reasons for which
residual bias exists and develop a new pipeline, MDR Cluster-Debias, to
mitigate this bias. We explore the strengths and weaknesses of our method,
finding that it significantly outperforms other existing debiasing approaches
on a variety of upstream bias tests but achieves limited improvement on
decreasing gender bias in a downstream task. This indicates that word
embeddings encode gender bias in still other ways, not necessarily captured by
upstream tests.