---
layout: publication
title: 'DWE+: Dual-way Matching Enhanced Framework For Multimodal Entity Linking'
authors: Shezheng Song, Shasha Li, Shan Zhao, Xiaopeng Li, Chengyu Wang, Jie Yu, Jun
  Ma, Tianwei Yan, Bin Ji, Xiaoguang Mao
conference: Arxiv
year: 2024
bibkey: song2024dwe
citations: 0
additional_links: [{name: Code, url: 'https://github.com/season1blue/DWET'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.04818'}]
tags: []
short_authors: Song et al.
---
Multimodal entity linking (MEL) aims to utilize multimodal information
(usually textual and visual information) to link ambiguous mentions to
unambiguous entities in knowledge base. Current methods facing main issues:
(1)treating the entire image as input may contain redundant information. (2)the
insufficient utilization of entity-related information, such as attributes in
images. (3)semantic inconsistency between the entity in knowledge base and its
representation. To this end, we propose DWE+ for multimodal entity linking.
DWE+ could capture finer semantics and dynamically maintain semantic
consistency with entities. This is achieved by three aspects: (a)we introduce a
method for extracting fine-grained image features by partitioning the image
into multiple local objects. Then, hierarchical contrastive learning is used to
further align semantics between coarse-grained information(text and image) and
fine-grained (mention and visual objects). (b)we explore ways to extract visual
attributes from images to enhance fusion feature such as facial features and
identity. (c)we leverage Wikipedia and ChatGPT to capture the entity
representation, achieving semantic enrichment from both static and dynamic
perspectives, which better reflects the real-world entity semantics.
Experiments on Wikimel, Richpedia, and Wikidiverse datasets demonstrate the
effectiveness of DWE+ in improving MEL performance. Specifically, we optimize
these datasets and achieve state-of-the-art performance on the enhanced
datasets. The code and enhanced datasets are released on
https://github.com/season1blue/DWET