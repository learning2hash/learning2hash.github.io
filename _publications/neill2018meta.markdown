---
layout: publication
title: Meta-embedding As Auxiliary Task Regularization
authors: James O' Neill, Danushka Bollegala
conference: Frontiers in Artificial Intelligence and Applications
year: 2020
bibkey: neill2018meta
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.05886'}]
tags: ["Self-Supervised"]
short_authors: James O' Neill, Danushka Bollegala
---
Word embeddings have been shown to benefit from ensambling several word
embedding sources, often carried out using straightforward mathematical
operations over the set of word vectors. More recently, self-supervised
learning has been used to find a lower-dimensional representation, similar in
size to the individual word embeddings within the ensemble. However, these
methods do not use the available manually labeled datasets that are often used
solely for the purpose of evaluation. We propose to reconstruct an ensemble of
word embeddings as an auxiliary task that regularises a main task while both
tasks share the learned meta-embedding layer. We carry out intrinsic evaluation
(6 word similarity datasets and 3 analogy datasets) and extrinsic evaluation (4
downstream tasks). For intrinsic task evaluation, supervision comes from
various labeled word similarity datasets. Our experimental results show that
the performance is improved for all word similarity datasets when compared to
self-supervised learning methods with a mean increase of \\(11.33\\) in Spearman
correlation. Specifically, the proposed method shows the best performance in 4
out of 6 of word similarity datasets when using a cosine reconstruction loss
and Brier's word similarity loss. Moreover, improvements are also made when
performing word meta-embedding reconstruction in sequence tagging and sentence
meta-embedding for sentence classification.