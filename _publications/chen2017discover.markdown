---
layout: publication
title: Discover And Learn New Objects From Documentaries
authors: Kai Chen, Hang Song, Chen Change Loy, Dahua Lin
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: chen2017discover
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.09593'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
Despite the remarkable progress in recent years, detecting objects in a new
context remains a challenging task. Detectors learned from a public dataset can
only work with a fixed list of categories, while training from scratch usually
requires a large amount of training data with detailed annotations. This work
aims to explore a novel approach -- learning object detectors from documentary
films in a weakly supervised manner. This is inspired by the observation that
documentaries often provide dedicated exposition of certain object categories,
where visual presentations are aligned with subtitles. We believe that object
detectors can be learned from such a rich source of information. Towards this
goal, we develop a joint probabilistic framework, where individual pieces of
information, including video frames and subtitles, are brought together via
both visual and linguistic links. On top of this formulation, we further derive
a weakly supervised learning algorithm, where object model learning and
training set mining are unified in an optimization procedure. Experimental
results on a real world dataset demonstrate that this is an effective approach
to learning new object detectors.