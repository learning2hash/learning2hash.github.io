---
layout: publication
title: Learning With Free Object Segments For Long-tailed Instance Segmentation
authors: Cheng Zhang, Tai-Yu Pan, Tianle Chen, Jike Zhong, Wenjin Fu, Wei-Lun Chao
conference: Lecture Notes in Computer Science
year: 2022
bibkey: zhang2022learning
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.11124'}]
tags: []
short_authors: Zhang et al.
---
One fundamental challenge in building an instance segmentation model for a
large number of classes in complex scenes is the lack of training examples,
especially for rare objects. In this paper, we explore the possibility to
increase the training examples without laborious data collection and
annotation. We find that an abundance of instance segments can potentially be
obtained freely from object-centric images, according to two insights: (i) an
object-centric image usually contains one salient object in a simple
background; (ii) objects from the same class often share similar appearances or
similar contrasts to the background. Motivated by these insights, we propose a
simple and scalable framework FreeSeg for extracting and leveraging these
"free" object foreground segments to facilitate model training in long-tailed
instance segmentation. Concretely, we investigate the similarity among
object-centric images of the same class to propose candidate segments of
foreground instances, followed by a novel ranking of segment quality. The
resulting high-quality object segments can then be used to augment the existing
long-tailed datasets, e.g., by copying and pasting the segments onto the
original training images. Extensive experiments show that FreeSeg yields
substantial improvements on top of strong baselines and achieves
state-of-the-art accuracy for segmenting rare object categories.