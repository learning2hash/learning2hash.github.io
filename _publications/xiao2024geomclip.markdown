---
layout: publication
title: 'Geomclip: Contrastive Geometry-text Pre-training For Molecules'
authors: Teng Xiao, Chao Cui, Huaisheng Zhu, Vasant G. Honavar
conference: 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)
year: 2024
bibkey: xiao2024geomclip
citations: 0
additional_links: [{name: Code, url: 'https://github.com/xiaocui3737/GeomCLIP'}, {
    name: Paper, url: 'https://arxiv.org/abs/2411.10821'}]
tags: [Tools & Libraries, Few-shot & Zero-shot, Datasets]
short_authors: Xiao et al.
---
Pretraining molecular representations is crucial for drug and material
discovery. Recent methods focus on learning representations from geometric
structures, effectively capturing 3D position information. Yet, they overlook
the rich information in biomedical texts, which detail molecules' properties
and substructures. With this in mind, we set up a data collection effort for
200K pairs of ground-state geometric structures and biomedical texts, resulting
in a PubChem3D dataset. Based on this dataset, we propose the GeomCLIP
framework to enhance for multi-modal representation learning from molecular
structures and biomedical text. During pre-training, we design two types of
tasks, i.e., multimodal representation alignment and unimodal denoising
pretraining, to align the 3D geometric encoder with textual information and, at
the same time, preserve its original representation power. Experimental results
show the effectiveness of GeomCLIP in various tasks such as molecular property
prediction, zero-shot text-molecule retrieval, and 3D molecule captioning. Our
code and collected dataset are available at
https://github.com/xiaocui3737/GeomCLIP