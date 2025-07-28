---
layout: publication
title: 'Seqnet: Learning Descriptors For Sequence-based Hierarchical Place Recognition'
authors: Sourav Garg, Michael Milford
conference: IEEE Robotics and Automation Letters
year: 2021
bibkey: garg2021seqnet
citations: 80
additional_links: [{name: Code, url: 'https://github.com/oravus/seqNet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2102.11603'}]
tags: ["Datasets", "Evaluation"]
short_authors: Sourav Garg, Michael Milford
---
Visual Place Recognition (VPR) is the task of matching current visual imagery
from a camera to images stored in a reference map of the environment. While
initial VPR systems used simple direct image methods or hand-crafted visual
features, recent work has focused on learning more powerful visual features and
further improving performance through either some form of sequential matcher /
filter or a hierarchical matching process. In both cases the performance of the
initial single-image based system is still far from perfect, putting
significant pressure on the sequence matching or (in the case of hierarchical
systems) pose refinement stages. In this paper we present a novel hybrid system
that creates a high performance initial match hypothesis generator using short
learnt sequential descriptors, which enable selective control sequential score
aggregation using single image learnt descriptors. Sequential descriptors are
generated using a temporal convolutional network dubbed SeqNet, encoding short
image sequences using 1-D convolutions, which are then matched against the
corresponding temporal descriptors from the reference dataset to provide an
ordered list of place match hypotheses. We then perform selective sequential
score aggregation using shortlisted single image learnt descriptors from a
separate pipeline to produce an overall place match hypothesis. Comprehensive
experiments on challenging benchmark datasets demonstrate the proposed method
outperforming recent state-of-the-art methods using the same amount of
sequential information. Source code and supplementary material can be found at
https://github.com/oravus/seqNet.