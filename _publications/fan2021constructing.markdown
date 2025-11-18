---
layout: publication
title: Constructing Phrase-level Semantic Labels To Form Multi-grained Supervision
  For Image-text Retrieval
authors: Zhihao Fan, Zhongyu Wei, Zejun Li, Siyuan Wang, Haijun Shan, Xuanjing Huang,
  Jianqing Fan
conference: 'ICMR ''22: International Conference on Multimedia Retrieval'
year: 2021
bibkey: fan2021constructing
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.05523'}]
tags: ["Multimodal Retrieval", "Text Retrieval"]
short_authors: Fan et al.
---
Existing research for image text retrieval mainly relies on sentence-level
supervision to distinguish matched and mismatched sentences for a query image.
However, semantic mismatch between an image and sentences usually happens in
finer grain, i.e., phrase level. In this paper, we explore to introduce
additional phrase-level supervision for the better identification of mismatched
units in the text. In practice, multi-grained semantic labels are automatically
constructed for a query image in both sentence-level and phrase-level. We
construct text scene graphs for the matched sentences and extract entities and
triples as the phrase-level labels. In order to integrate both supervision of
sentence-level and phrase-level, we propose Semantic Structure Aware Multimodal
Transformer (SSAMT) for multi-modal representation learning. Inside the SSAMT,
we utilize different kinds of attention mechanisms to enforce interactions of
multi-grain semantic units in both sides of vision and language. For the
training, we propose multi-scale matching losses from both global and local
perspectives, and penalize mismatched phrases. Experimental results on MS-COCO
and Flickr30K show the effectiveness of our approach compared to some
state-of-the-art models.