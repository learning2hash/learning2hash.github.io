---
layout: publication
title: Learning To Generate Scene Graph From Natural Language Supervision
authors: Yiwu Zhong, Jing Shi, Jianwei Yang, Chenliang Xu, Yin Li
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: zhong2021learning
citations: 58
additional_links: [{name: Code, url: 'https://github.com/YiwuZhong/SGG_from_NLS'},
  {name: Paper, url: 'https://arxiv.org/abs/2109.02227'}]
tags: ["ICCV", "Supervised"]
short_authors: Zhong et al.
---
Learning from image-text data has demonstrated recent success for many
recognition tasks, yet is currently limited to visual features or individual
visual concepts such as objects. In this paper, we propose one of the first
methods that learn from image-sentence pairs to extract a graphical
representation of localized objects and their relationships within an image,
known as scene graph. To bridge the gap between images and texts, we leverage
an off-the-shelf object detector to identify and localize object instances,
match labels of detected regions to concepts parsed from captions, and thus
create "pseudo" labels for learning scene graph. Further, we design a
Transformer-based model to predict these "pseudo" labels via a masked token
prediction task. Learning from only image-sentence pairs, our model achieves
30% relative gain over a latest method trained with human-annotated unlocalized
scene graphs. Our model also shows strong results for weakly and fully
supervised scene graph generation. In addition, we explore an open-vocabulary
setting for detecting scene graphs, and present the first result for open-set
scene graph generation. Our code is available at
https://github.com/YiwuZhong/SGG_from_NLS.