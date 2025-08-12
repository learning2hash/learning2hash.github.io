---
layout: publication
title: 'Few-nerd: A Few-shot Named Entity Recognition Dataset'
authors: Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Hai-Tao
  Zheng, Zhiyuan Liu
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: ding2021few
citations: 161
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.07464'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Ding et al.
---
Recently, considerable literature has grown up around the theme of few-shot
named entity recognition (NER), but little published benchmark data
specifically focused on the practical and challenging task. Current approaches
collect existing supervised NER datasets and re-organize them to the few-shot
setting for empirical study. These strategies conventionally aim to recognize
coarse-grained entity types with few examples, while in practice, most unseen
entity types are fine-grained. In this paper, we present Few-NERD, a
large-scale human-annotated few-shot NER dataset with a hierarchy of 8
coarse-grained and 66 fine-grained entity types. Few-NERD consists of 188,238
sentences from Wikipedia, 4,601,160 words are included and each is annotated as
context or a part of a two-level entity type. To the best of our knowledge,
this is the first few-shot NER dataset and the largest human-crafted NER
dataset. We construct benchmark tasks with different emphases to
comprehensively assess the generalization capability of models. Extensive
empirical results and analysis show that Few-NERD is challenging and the
problem requires further research. We make Few-NERD public at
https://ningding97.github.io/fewnerd/.