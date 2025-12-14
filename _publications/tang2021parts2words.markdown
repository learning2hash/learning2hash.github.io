---
layout: publication
title: 'Parts2words: Learning Joint Embedding Of Point Clouds And Texts By Bidirectional
  Matching Between Parts And Words'
authors: Chuan Tang, Xi Yang, Bojian Wu, Zhizhong Han, Yi Chang
conference: Arxiv
year: 2021
bibkey: tang2021parts2words
citations: 0
additional_links: [{name: Code, url: 'https://github.com/JLUtangchuan/Parts2Words'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.01872'}]
tags: [Datasets]
short_authors: Tang et al.
---
Shape-Text matching is an important task of high-level shape understanding.
Current methods mainly represent a 3D shape as multiple 2D rendered views,
which obviously can not be understood well due to the structural ambiguity
caused by self-occlusion in the limited number of views. To resolve this issue,
we directly represent 3D shapes as point clouds, and propose to learn joint
embedding of point clouds and texts by bidirectional matching between parts
from shapes and words from texts. Specifically, we first segment the point
clouds into parts, and then leverage optimal transport method to match parts
and words in an optimized feature space, where each part is represented by
aggregating features of all points within it and each word is abstracted by its
contextual information. We optimize the feature space in order to enlarge the
similarities between the paired training samples, while simultaneously
maximizing the margin between the unpaired ones. Experiments demonstrate that
our method achieves a significant improvement in accuracy over the SOTAs on
multi-modal retrieval tasks under the Text2Shape dataset. Codes are available
at https://github.com/JLUtangchuan/Parts2Words.