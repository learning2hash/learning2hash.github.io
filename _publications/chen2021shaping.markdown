---
layout: publication
title: Shaping Visual Representations With Attributes For Few-shot Recognition
authors: Haoxing Chen, Huaxiong Li, Yaohui Li, Chunlin Chen
conference: IEEE Signal Processing Letters
year: 2022
bibkey: chen2021shaping
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.06398'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Few-shot recognition aims to recognize novel categories under low-data
regimes. Some recent few-shot recognition methods introduce auxiliary semantic
modality, i.e., category attribute information, into representation learning,
which enhances the feature discrimination and improves the recognition
performance. Most of these existing methods only consider the attribute
information of support set while ignoring the query set, resulting in a
potential loss of performance. In this letter, we propose a novel
attribute-shaped learning (ASL) framework, which can jointly perform query
attributes generation and discriminative visual representation learning for
few-shot recognition. Specifically, a visual-attribute predictor (VAP) is
constructed to predict the attributes of queries. By leveraging the attributes
information, an attribute-visual attention module (AVAM) is designed, which can
adaptively utilize attributes and visual representations to learn more
discriminative features. Under the guidance of attribute modality, our method
can learn enhanced semantic-aware representation for classification.
Experiments demonstrate that our method can achieve competitive results on CUB
and SUN benchmarks. Our source code is available at:
https://github.com/chenhaoxing/ASL.