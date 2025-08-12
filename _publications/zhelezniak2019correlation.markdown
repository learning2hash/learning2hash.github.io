---
layout: publication
title: Correlation Coefficients And Semantic Textual Similarity
authors: Vitalii Zhelezniak, Aleksandar Savkov, April Shen, Nils Y. Hammerla
conference: Proceedings of the 2019 Conference of the North
year: 2019
bibkey: zhelezniak2019correlation
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.07790'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Zhelezniak et al.
---
A large body of research into semantic textual similarity has focused on
constructing state-of-the-art embeddings using sophisticated modelling, careful
choice of learning signals and many clever tricks. By contrast, little
attention has been devoted to similarity measures between these embeddings,
with cosine similarity being used unquestionably in the majority of cases. In
this work, we illustrate that for all common word vectors, cosine similarity is
essentially equivalent to the Pearson correlation coefficient, which provides
some justification for its use. We thoroughly characterise cases where Pearson
correlation (and thus cosine similarity) is unfit as similarity measure.
Importantly, we show that Pearson correlation is appropriate for some word
vectors but not others. When it is not appropriate, we illustrate how common
non-parametric rank correlation coefficients can be used instead to
significantly improve performance. We support our analysis with a series of
evaluations on word-level and sentence-level semantic textual similarity
benchmarks. On the latter, we show that even the simplest averaged word vectors
compared by rank correlation easily rival the strongest deep representations
compared by cosine similarity.