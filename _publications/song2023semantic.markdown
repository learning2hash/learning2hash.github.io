---
layout: publication
title: Semantic-embedded Similarity Prototype For Scene Recognition
authors: Chuanxin Song, Hanbo Wu, Xin Ma, Yibin Li
conference: Pattern Recognition
year: 2024
bibkey: song2023semantic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.05896'}]
tags: ["Distance Metric Learning"]
short_authors: Song et al.
---
Due to the high inter-class similarity caused by the complex composition and
the co-existing objects across scenes, numerous studies have explored object
semantic knowledge within scenes to improve scene recognition. However, a
resulting challenge emerges as object information extraction techniques require
heavy computational costs, thereby burdening the network considerably. This
limitation often renders object-assisted approaches incompatible with edge
devices in practical deployment. In contrast, this paper proposes a semantic
knowledge-based similarity prototype, which can help the scene recognition
network achieve superior accuracy without increasing the computational cost in
practice. It is simple and can be plug-and-played into existing pipelines. More
specifically, a statistical strategy is introduced to depict semantic knowledge
in scenes as class-level semantic representations. These representations are
used to explore correlations between scene classes, ultimately constructing a
similarity prototype. Furthermore, we propose to leverage the similarity
prototype to support network training from the perspective of Gradient Label
Softening and Batch-level Contrastive Loss, respectively. Comprehensive
evaluations on multiple benchmarks show that our similarity prototype enhances
the performance of existing networks, all while avoiding any additional
computational burden in practical deployments. Code and the statistical
similarity prototype will be available at
https://github.com/ChuanxinSong/SimilarityPrototype