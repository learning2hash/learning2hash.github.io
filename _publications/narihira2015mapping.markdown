---
layout: publication
title: Mapping Images To Sentiment Adjective Noun Pairs With Factorized Neural Nets
authors: Takuya Narihira, Damian Borth, Stella X. Yu, Karl Ni, Trevor Darrell
conference: Arxiv
year: 2015
bibkey: narihira2015mapping
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.06838'}]
tags: []
short_authors: Narihira et al.
---
We consider the visual sentiment task of mapping an image to an adjective
noun pair (ANP) such as "cute baby". To capture the two-factor structure of our
ANP semantics as well as to overcome annotation noise and ambiguity, we propose
a novel factorized CNN model which learns separate representations for
adjectives and nouns but optimizes the classification performance over their
product. Our experiments on the publicly available SentiBank dataset show that
our model significantly outperforms not only independent ANP classifiers on
unseen ANPs and on retrieving images of novel ANPs, but also image captioning
models which capture word semantics from co-occurrence of natural text; the
latter turn out to be surprisingly poor at capturing the sentiment evoked by
pure visual experience. That is, our factorized ANP CNN not only trains better
from noisy labels, generalizes better to new images, but can also expands the
ANP vocabulary on its own.