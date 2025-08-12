---
layout: publication
title: 'Open-world Instance Segmentation: Exploiting Pseudo Ground Truth From Learned
  Pairwise Affinity'
authors: Weiyao Wang, Matt Feiszli, Heng Wang, Jitendra Malik, Du Tran
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: wang2022open
citations: 26
additional_links: [{name: Code, url: 'https://sites.google.com/view/generic-grouping/'},
  {name: Paper, url: 'https://arxiv.org/abs/2204.06107'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: Wang et al.
---
Open-world instance segmentation is the task of grouping pixels into object
instances without any pre-determined taxonomy. This is challenging, as
state-of-the-art methods rely on explicit class semantics obtained from large
labeled datasets, and out-of-domain evaluation performance drops significantly.
Here we propose a novel approach for mask proposals, Generic Grouping Networks
(GGNs), constructed without semantic supervision. Our approach combines a local
measure of pixel affinity with instance-level mask supervision, producing a
training regimen designed to make the model as generic as the data diversity
allows. We introduce a method for predicting Pairwise Affinities (PA), a
learned local relationship between pairs of pixels. PA generalizes very well to
unseen categories. From PA we construct a large set of pseudo-ground-truth
instance masks; combined with human-annotated instance masks we train GGNs and
significantly outperform the SOTA on open-world instance segmentation on
various benchmarks including COCO, LVIS, ADE20K, and UVO. Code is available on
project website: https://sites.google.com/view/generic-grouping/.