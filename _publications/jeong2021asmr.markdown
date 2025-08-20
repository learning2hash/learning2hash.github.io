---
layout: publication
title: 'ASMR: Learning Attribute-based Person Search With Adaptive Semantic Margin
  Regularizer'
authors: Boseung Jeong, Jicheol Park, Suha Kwak
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: jeong2021asmr
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04533'}]
tags: [Distance Metric Learning, ICCV]
short_authors: Boseung Jeong, Jicheol Park, Suha Kwak
---
Attribute-based person search is the task of finding person images that are
best matched with a set of text attributes given as query. The main challenge
of this task is the large modality gap between attributes and images. To reduce
the gap, we present a new loss for learning cross-modal embeddings in the
context of attribute-based person search. We regard a set of attributes as a
category of people sharing the same traits. In a joint embedding space of the
two modalities, our loss pulls images close to their person categories for
modality alignment. More importantly, it pushes apart a pair of person
categories by a margin determined adaptively by their semantic distance, where
the distance metric is learned end-to-end so that the loss considers importance
of each attribute when relating person categories. Our loss guided by the
adaptive semantic margin leads to more discriminative and semantically
well-arranged distributions of person images. As a consequence, it enables a
simple embedding model to achieve state-of-the-art records on public benchmarks
without bells and whistles.