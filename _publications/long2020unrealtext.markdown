---
layout: publication
title: 'Unrealtext: Synthesizing Realistic Scene Text Images From The Unreal World'
authors: Shangbang Long, Cong Yao
conference: Arxiv
year: 2020
bibkey: long2020unrealtext
citations: 47
additional_links: [{name: Code, url: 'https://github.com/Jyouhou/UnrealText/'}, {
    name: Paper, url: 'https://arxiv.org/abs/2003.10608'}]
tags: ["Datasets"]
short_authors: Shangbang Long, Cong Yao
---
Synthetic data has been a critical tool for training scene text detection and
recognition models. On the one hand, synthetic word images have proven to be a
successful substitute for real images in training scene text recognizers. On
the other hand, however, scene text detectors still heavily rely on a large
amount of manually annotated real-world images, which are expensive. In this
paper, we introduce UnrealText, an efficient image synthesis method that
renders realistic images via a 3D graphics engine. 3D synthetic engine provides
realistic appearance by rendering scene and text as a whole, and allows for
better text region proposals with access to precise scene information, e.g.
normal and even object meshes. The comprehensive experiments verify its
effectiveness on both scene text detection and recognition. We also generate a
multilingual version for future research into multilingual scene text detection
and recognition. Additionally, we re-annotate scene text recognition datasets
in a case-sensitive way and include punctuation marks for more comprehensive
evaluations. The code and the generated datasets are released at:
https://github.com/Jyouhou/UnrealText/ .