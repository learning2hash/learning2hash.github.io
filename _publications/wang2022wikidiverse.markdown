---
layout: publication
title: 'Wikidiverse: A Multimodal Entity Linking Dataset With Diversified Contextual
  Topics And Entity Types'
authors: Xuwu Wang, Junfeng Tian, Min Gui, Zhixu Li, Rui Wang, Ming Yan, Lihan Chen,
  Yanghua Xiao
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: wang2022wikidiverse
citations: 24
additional_links: [{name: Code, url: 'https://github.com/wangxw5/wikiDiverse'}, {
    name: Paper, url: 'https://arxiv.org/abs/2204.06347'}]
tags: ["Datasets"]
short_authors: Wang et al.
---
Multimodal Entity Linking (MEL) which aims at linking mentions with
multimodal contexts to the referent entities from a knowledge base (e.g.,
Wikipedia), is an essential task for many multimodal applications. Although
much attention has been paid to MEL, the shortcomings of existing MEL datasets
including limited contextual topics and entity types, simplified mention
ambiguity, and restricted availability, have caused great obstacles to the
research and application of MEL. In this paper, we present WikiDiverse, a
high-quality human-annotated MEL dataset with diversified contextual topics and
entity types from Wikinews, which uses Wikipedia as the corresponding knowledge
base. A well-tailored annotation procedure is adopted to ensure the quality of
the dataset. Based on WikiDiverse, a sequence of well-designed MEL models with
intra-modality and inter-modality attentions are implemented, which utilize the
visual information of images more adequately than existing MEL models do.
Extensive experimental analyses are conducted to investigate the contributions
of different modalities in terms of MEL, facilitating the future research on
this task. The dataset and baseline models are available at
https://github.com/wangxw5/wikiDiverse.