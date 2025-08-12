---
layout: publication
title: A Novel Visual Word Co-occurrence Model For Person Re-identification
authors: Ziming Zhang, Yuting Chen, Venkatesh Saligrama
conference: Lecture Notes in Computer Science
year: 2015
bibkey: zhang2014novel
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1410.6532'}]
tags: []
short_authors: Ziming Zhang, Yuting Chen, Venkatesh Saligrama
---
Person re-identification aims to maintain the identity of an individual in
diverse locations through different non-overlapping camera views. The problem
is fundamentally challenging due to appearance variations resulting from
differing poses, illumination and configurations of camera views. To deal with
these difficulties, we propose a novel visual word co-occurrence model. We
first map each pixel of an image to a visual word using a codebook, which is
learned in an unsupervised manner. The appearance transformation between camera
views is encoded by a co-occurrence matrix of visual word joint distributions
in probe and gallery images. Our appearance model naturally accounts for
spatial similarities and variations caused by pose, illumination &
configuration change across camera views. Linear SVMs are then trained as
classifiers using these co-occurrence descriptors. On the VIPeR and CUHK Campus
benchmark datasets, our method achieves 83.86% and 85.49% at rank-15 on the
Cumulative Match Characteristic (CMC) curves, and beats the state-of-the-art
results by 10.44% and 22.27%.