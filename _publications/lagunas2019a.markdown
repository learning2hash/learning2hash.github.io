---
layout: publication
title: A Similarity Measure For Material Appearance
authors: Manuel Lagunas, Sandra Malpica, Ana Serrano, Elena Garces, Diego Gutierrez,
  Belen Masia
conference: ACM Transactions on Graphics
year: 2019
bibkey: lagunas2019a
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.01562'}]
tags: [Neural Hashing, Evaluation]
short_authors: Lagunas et al.
---
We present a model to measure the similarity in appearance between different
materials, which correlates with human similarity judgments. We first create a
database of 9,000 rendered images depicting objects with varying materials,
shape and illumination. We then gather data on perceived similarity from
crowdsourced experiments; our analysis of over 114,840 answers suggests that
indeed a shared perception of appearance similarity exists. We feed this data
to a deep learning architecture with a novel loss function, which learns a
feature space for materials that correlates with such perceived appearance
similarity. Our evaluation shows that our model outperforms existing metrics.
Last, we demonstrate several applications enabled by our metric, including
appearance-based search for material suggestions, database visualization,
clustering and summarization, and gamut mapping.