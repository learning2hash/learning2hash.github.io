---
layout: publication
title: A Universal Representation Transformer Layer For Few-shot Image Classification
authors: Lu Liu, William Hamilton, Guodong Long, Jing Jiang, Hugo Larochelle
conference: Arxiv
year: 2020
bibkey: liu2020universal
citations: 56
additional_links: [{name: Code, url: 'https://github.com/liulu112601/URT'}, {name: Paper,
    url: 'https://arxiv.org/abs/2006.11702'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot classification aims to recognize unseen classes when presented with
only a small number of samples. We consider the problem of multi-domain
few-shot image classification, where unseen classes and examples come from
diverse data sources. This problem has seen growing interest and has inspired
the development of benchmarks such as Meta-Dataset. A key challenge in this
multi-domain setting is to effectively integrate the feature representations
from the diverse set of training domains. Here, we propose a Universal
Representation Transformer (URT) layer, that meta-learns to leverage universal
features for few-shot classification by dynamically re-weighting and composing
the most appropriate domain-specific representations. In experiments, we show
that URT sets a new state-of-the-art result on Meta-Dataset. Specifically, it
achieves top-performance on the highest number of data sources compared to
competing methods. We analyze variants of URT and present a visualization of
the attention score heatmaps that sheds light on how the model performs
cross-domain generalization. Our code is available at
https://github.com/liulu112601/URT.