---
layout: publication
title: Ensemble Of Part Detectors For Simultaneous Classification And Localization
authors: Xiaopeng Zhang, Hongkai Xiong, Weiyao Lin, Qi Tian
conference: Arxiv
year: 2017
bibkey: zhang2017ensemble
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10034'}]
tags: []
short_authors: Zhang et al.
---
Part-based representation has been proven to be effective for a variety of
visual applications. However, automatic discovery of discriminative parts
without object/part-level annotations is challenging. This paper proposes a
discriminative mid-level representation paradigm based on the responses of a
collection of part detectors, which only requires the image-level labels.
Towards this goal, we first develop a detector-based spectral clustering method
to mine the representative and discriminative mid-level patterns for detector
initialization. The advantage of the proposed pattern mining technology is that
the distance metric based on detectors only focuses on discriminative details,
and a set of such grouped detectors offer an effective way for consistent
pattern mining. Relying on the discovered patterns, we further formulate the
detector learning process as a confidence-loss sparse Multiple Instance
Learning (cls-MIL) task, which considers the diversity of the positive samples,
while avoid drifting away the well localized ones by assigning a confidence
value to each positive sample. The responses of the learned detectors can form
an effective mid-level image representation for both image classification and
object localization. Experiments conducted on benchmark datasets demonstrate
the superiority of our method over existing approaches.