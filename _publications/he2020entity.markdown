---
layout: publication
title: Entity Candidate Network For Whole-aware Named Entity Recognition
authors: Wendong He, Yizhen Shao, Pingjian Zhang
conference: Arxiv
year: 2020
bibkey: he2020entity
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.14145'}]
tags: []
short_authors: Wendong He, Yizhen Shao, Pingjian Zhang
---
Named Entity Recognition (NER) is a crucial upstream task in Natural Language
Processing (NLP). Traditional tag scheme approaches offer a single recognition
that does not meet the needs of many downstream tasks such as coreference
resolution. Meanwhile, Tag scheme approaches ignore the continuity of entities.
Inspired by one-stage object detection models in computer vision (CV), this
paper proposes a new no-tag scheme, the Whole-Aware Detection, which makes NER
an object detection task. Meanwhile, this paper presents a novel model, Entity
Candidate Network (ECNet), and a specific convolution network, Adaptive Context
Convolution Network (ACCN), to fuse multi-scale contexts and encode entity
information at each position. ECNet identifies the full span of a named entity
and its type at each position based on Entity Loss. Furthermore, ECNet is
regulable between the highest precision and the highest recall, while the tag
scheme approaches are not. Experimental results on the CoNLL 2003 English
dataset and the WNUT 2017 dataset show that ECNet outperforms other previous
state-of-the-art methods.