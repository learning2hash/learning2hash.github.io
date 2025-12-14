---
layout: publication
title: 'Beat: Bi-directional One-to-many Embedding Alignment For Text-based Person
  Retrieval'
authors: Yiwei Ma, Xiaoshuai Sun, Jiayi Ji, Guannan Jiang, Weilin Zhuang, Rongrong
  Ji
conference: Arxiv
year: 2024
bibkey: ma2024beat
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.05620'}]
tags: [Text Retrieval, Evaluation, Datasets]
short_authors: Ma et al.
---
Text-based person retrieval (TPR) is a challenging task that involves
retrieving a specific individual based on a textual description. Despite
considerable efforts to bridge the gap between vision and language, the
significant differences between these modalities continue to pose a challenge.
Previous methods have attempted to align text and image samples in a
modal-shared space, but they face uncertainties in optimization directions due
to the movable features of both modalities and the failure to account for
one-to-many relationships of image-text pairs in TPR datasets. To address this
issue, we propose an effective bi-directional one-to-many embedding paradigm
that offers a clear optimization direction for each sample, thus mitigating the
optimization problem. Additionally, this embedding scheme generates multiple
features for each sample without introducing trainable parameters, making it
easier to align with several positive samples. Based on this paradigm, we
propose a novel Bi-directional one-to-many Embedding Alignment (Beat) model to
address the TPR task. Our experimental results demonstrate that the proposed
Beat model achieves state-of-the-art performance on three popular TPR datasets,
including CUHK-PEDES (65.61 R@1), ICFG-PEDES (58.25 R@1), and RSTPReID (48.10
R@1). Furthermore, additional experiments on MS-COCO, CUB, and Flowers datasets
further demonstrate the potential of Beat to be applied to other image-text
retrieval tasks.