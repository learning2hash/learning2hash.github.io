---
layout: publication
title: Gender Bias In Meta-embeddings
authors: Masahiro Kaneko, Danushka Bollegala, Naoaki Okazaki
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2022'
year: 2022
bibkey: kaneko2022gender
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.09867'}]
tags: ["EMNLP"]
short_authors: Masahiro Kaneko, Danushka Bollegala, Naoaki Okazaki
---
Different methods have been proposed to develop meta-embeddings from a given
set of source embeddings. However, the source embeddings can contain unfair
gender-related biases, and how these influence the meta-embeddings has not been
studied yet. We study the gender bias in meta-embeddings created under three
different settings: (1) meta-embedding multiple sources without performing any
debiasing (Multi-Source No-Debiasing), (2) meta-embedding multiple sources
debiased by a single method (Multi-Source Single-Debiasing), and (3)
meta-embedding a single source debiased by different methods (Single-Source
Multi-Debiasing). Our experimental results show that meta-embedding amplifies
the gender biases compared to input source embeddings. We find that debiasing
not only the sources but also their meta-embedding is needed to mitigate those
biases. Moreover, we propose a novel debiasing method based on meta-embedding
learning where we use multiple debiasing methods on a single source embedding
and then create a single unbiased meta-embedding.