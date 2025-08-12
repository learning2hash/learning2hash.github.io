---
layout: publication
title: Persistence Codebooks For Topological Data Analysis
authors: Bartosz Zielinski, Michal Lipinski, Mateusz Juda, Matthias Zeppelzauer, Pawel
  Dlotko
conference: Artificial Intelligence Review
year: 2020
bibkey: zielinski2018persistence
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.04852'}]
tags: []
short_authors: Zielinski et al.
---
Persistent homology (PH) is a rigorous mathematical theory that provides a
robust descriptor of data in the form of persistence diagrams (PDs) which are
2D multisets of points. Their variable size makes them, however, difficult to
combine with typical machine learning workflows. In this paper we introduce
persistence codebooks, a novel expressive and discriminative fixed-size
vectorized representation of PDs. To this end, we adapt bag-of-words (BoW),
vectors of locally aggregated descriptors (VLAD) and Fischer vectors (FV) for
the quantization of PDs. Persistence codebooks represent PDs in a convenient
way for machine learning and statistical analysis and have a number of
favorable practical and theoretical properties including 1-Wasserstein
stability. We evaluate the presented representations on several heterogeneous
datasets and show their (high) discriminative power. Our approach achieves
state-of-the-art performance and beyond in much less time than alternative
approaches.