---
layout: publication
title: Few-shot Text Classification With Distributional Signatures
authors: Yujia Bao, Menghua Wu, Shiyu Chang, Regina Barzilay
conference: Arxiv
year: 2019
bibkey: bao2019few
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.06039'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bao et al.
---
In this paper, we explore meta-learning for few-shot text classification.
Meta-learning has shown strong performance in computer vision, where low-level
patterns are transferable across learning tasks. However, directly applying
this approach to text is challenging--lexical features highly informative for
one task may be insignificant for another. Thus, rather than learning solely
from words, our model also leverages their distributional signatures, which
encode pertinent word occurrence patterns. Our model is trained within a
meta-learning framework to map these signatures into attention scores, which
are then used to weight the lexical representations of words. We demonstrate
that our model consistently outperforms prototypical networks learned on
lexical knowledge (Snell et al., 2017) in both few-shot text classification and
relation classification by a significant margin across six benchmark datasets
(20.0% on average in 1-shot classification).