---
layout: publication
title: 'Vldeformer: Vision-language Decomposed Transformer For Fast Cross-modal Retrieval'
authors: Lisai Zhang, Hongfa Wu, Qingcai Chen, Yimeng Deng, Zhonghua Li, Dejiang Kong,
  Zhao Cao, Joanna Siebert, Yunpeng Han
conference: Knowledge-Based Systems
year: 2022
bibkey: zhang2021vldeformer
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.11338'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Image Retrieval"]
short_authors: Zhang et al.
---
Cross-model retrieval has emerged as one of the most important upgrades for
text-only search engines (SE). Recently, with powerful representation for
pairwise text-image inputs via early interaction, the accuracy of
vision-language (VL) transformers has outperformed existing methods for
text-image retrieval. However, when the same paradigm is used for inference,
the efficiency of the VL transformers is still too low to be applied in a real
cross-modal SE. Inspired by the mechanism of human learning and using
cross-modal knowledge, this paper presents a novel Vision-Language Decomposed
Transformer (VLDeformer), which greatly increases the efficiency of VL
transformers while maintaining their outstanding accuracy. By the proposed
method, the cross-model retrieval is separated into two stages: the VL
transformer learning stage, and the VL decomposition stage. The latter stage
plays the role of single modal indexing, which is to some extent like the term
indexing of a text SE. The model learns cross-modal knowledge from
early-interaction pre-training and is then decomposed into an individual
encoder. The decomposition requires only small target datasets for supervision
and achieves both \(1000+\) times acceleration and less than \(0.6\)% average
recall drop. VLDeformer also outperforms state-of-the-art visual-semantic
embedding methods on COCO and Flickr30k.