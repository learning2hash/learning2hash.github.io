---
layout: publication
title: An Enhanced Span-based Decomposition Method For Few-shot Sequence Labeling
authors: Peiyi Wang, Runxin Xu, Tianyu Liu, Qingyu Zhou, Yunbo Cao, Baobao Chang,
  Zhifang Sui
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2022
bibkey: wang2021enhanced
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.13023'}]
tags: ["Few Shot & Zero Shot", "NAACL"]
short_authors: Wang et al.
---
Few-Shot Sequence Labeling (FSSL) is a canonical paradigm for the tagging
models, e.g., named entity recognition and slot filling, to generalize on an
emerging, resource-scarce domain. Recently, the metric-based meta-learning
framework has been recognized as a promising approach for FSSL. However, most
prior works assign a label to each token based on the token-level similarities,
which ignores the integrality of named entities or slots. To this end, in this
paper, we propose ESD, an Enhanced Span-based Decomposition method for FSSL.
ESD formulates FSSL as a span-level matching problem between test query and
supporting instances. Specifically, ESD decomposes the span matching problem
into a series of span-level procedures, mainly including enhanced span
representation, class prototype aggregation and span conflicts resolution.
Extensive experiments show that ESD achieves the new state-of-the-art results
on two popular FSSL benchmarks, FewNERD and SNIPS, and is proven to be more
robust in the nested and noisy tagging scenarios. Our code is available at
https://github.com/Wangpeiyi9979/ESD.