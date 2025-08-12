---
layout: publication
title: Cost Aggregation With 4D Convolutional Swin Transformer For Few-shot Segmentation
authors: Sunghwan Hong, Seokju Cho, Jisu Nam, Stephen Lin, Seungryong Kim
conference: Lecture Notes in Computer Science
year: 2022
bibkey: hong2022cost
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.10866'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hong et al.
---
This paper presents a novel cost aggregation network, called Volumetric
Aggregation with Transformers (VAT), for few-shot segmentation. The use of
transformers can benefit correlation map aggregation through self-attention
over a global receptive field. However, the tokenization of a correlation map
for transformer processing can be detrimental, because the discontinuity at
token boundaries reduces the local context available near the token edges and
decreases inductive bias. To address this problem, we propose a 4D
Convolutional Swin Transformer, where a high-dimensional Swin Transformer is
preceded by a series of small-kernel convolutions that impart local context to
all pixels and introduce convolutional inductive bias. We additionally boost
aggregation performance by applying transformers within a pyramidal structure,
where aggregation at a coarser level guides aggregation at a finer level. Noise
in the transformer output is then filtered in the subsequent decoder with the
help of the query's appearance embedding. With this model, a new
state-of-the-art is set for all the standard benchmarks in few-shot
segmentation. It is shown that VAT attains state-of-the-art performance for
semantic correspondence as well, where cost aggregation also plays a central
role.