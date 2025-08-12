---
layout: publication
title: Multi-modal Few-shot Temporal Action Detection
authors: Sauradip Nag, Mengmeng Xu, Xiatian Zhu, Juan-Manuel Perez-Rua, Bernard Ghanem,
  Yi-Zhe Song, Tao Xiang
conference: Arxiv
year: 2022
bibkey: nag2022multi
citations: 1
additional_links: [{name: Code, url: 'https://github.com/sauradip/MUPPET'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.14905'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Nag et al.
---
Few-shot (FS) and zero-shot (ZS) learning are two different approaches for
scaling temporal action detection (TAD) to new classes. The former adapts a
pretrained vision model to a new task represented by as few as a single video
per class, whilst the latter requires no training examples by exploiting a
semantic description of the new class. In this work, we introduce a new
multi-modality few-shot (MMFS) TAD problem, which can be considered as a
marriage of FS-TAD and ZS-TAD by leveraging few-shot support videos and new
class names jointly. To tackle this problem, we further introduce a novel
MUlti-modality PromPt mETa-learning (MUPPET) method. This is enabled by
efficiently bridging pretrained vision and language models whilst maximally
reusing already learned capacity. Concretely, we construct multi-modal prompts
by mapping support videos into the textual token space of a vision-language
model using a meta-learned adapter-equipped visual semantics tokenizer. To
tackle large intra-class variation, we further design a query feature
regulation scheme. Extensive experiments on ActivityNetv1.3 and THUMOS14
demonstrate that our MUPPET outperforms state-of-the-art alternative methods,
often by a large margin. We also show that our MUPPET can be easily extended to
tackle the few-shot object detection problem and again achieves the
state-of-the-art performance on MS-COCO dataset. The code will be available in
https://github.com/sauradip/MUPPET