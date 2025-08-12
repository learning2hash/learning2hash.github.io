---
layout: publication
title: 'Aerial Scene Understanding In The Wild: Multi-scene Recognition Via Prototype-based
  Memory Networks'
authors: Yuansheng Hua, Lichao Moua, Jianzhe Lin, Konrad Heidler, Xiao Xiang Zhu
conference: ISPRS Journal of Photogrammetry and Remote Sensing
year: 2021
bibkey: hua2021aerial
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.11200'}]
tags: ["Datasets"]
short_authors: Hua et al.
---
Aerial scene recognition is a fundamental visual task and has attracted an
increasing research interest in the last few years. Most of current researches
mainly deploy efforts to categorize an aerial image into one scene-level label,
while in real-world scenarios, there often exist multiple scenes in a single
image. Therefore, in this paper, we propose to take a step forward to a more
practical and challenging task, namely multi-scene recognition in single
images. Moreover, we note that manually yielding annotations for such a task is
extraordinarily time- and labor-consuming. To address this, we propose a
prototype-based memory network to recognize multiple scenes in a single image
by leveraging massive well-annotated single-scene images. The proposed network
consists of three key components: 1) a prototype learning module, 2) a
prototype-inhabiting external memory, and 3) a multi-head attention-based
memory retrieval module. To be more specific, we first learn the prototype
representation of each aerial scene from single-scene aerial image datasets and
store it in an external memory. Afterwards, a multi-head attention-based memory
retrieval module is devised to retrieve scene prototypes relevant to query
multi-scene images for final predictions. Notably, only a limited number of
annotated multi-scene images are needed in the training phase. To facilitate
the progress of aerial scene recognition, we produce a new multi-scene aerial
image (MAI) dataset. Experimental results on variant dataset configurations
demonstrate the effectiveness of our network. Our dataset and codes are
publicly available.