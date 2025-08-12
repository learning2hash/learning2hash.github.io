---
layout: publication
title: 'CSI: Novelty Detection Via Contrastive Learning On Distributionally Shifted
  Instances'
authors: Jihoon Tack, Sangwoo Mo, Jongheon Jeong, Jinwoo Shin
conference: Arxiv
year: 2020
bibkey: tack2020csi
citations: 214
additional_links: [{name: Code, url: 'https://github.com/alinlab/CSI'}, {name: Paper,
    url: 'https://arxiv.org/abs/2007.08176'}]
tags: ["Self-Supervised"]
short_authors: Tack et al.
---
Novelty detection, i.e., identifying whether a given sample is drawn from
outside the training distribution, is essential for reliable machine learning.
To this end, there have been many attempts at learning a representation
well-suited for novelty detection and designing a score based on such
representation. In this paper, we propose a simple, yet effective method named
contrasting shifted instances (CSI), inspired by the recent success on
contrastive learning of visual representations. Specifically, in addition to
contrasting a given sample with other instances as in conventional contrastive
learning methods, our training scheme contrasts the sample with
distributionally-shifted augmentations of itself. Based on this, we propose a
new detection score that is specific to the proposed training scheme. Our
experiments demonstrate the superiority of our method under various novelty
detection scenarios, including unlabeled one-class, unlabeled multi-class and
labeled multi-class settings, with various image benchmark datasets. Code and
pre-trained models are available at https://github.com/alinlab/CSI.