---
layout: publication
title: 'Vrr-vg: Refocusing Visually-relevant Relationships'
authors: Yuanzhi Liang, Yalong Bai, Wei Zhang, Xueming Qian, Li Zhu, Tao Mei
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: liang2019vrr
citations: 60
additional_links: [{name: Code, url: 'http://vrr-vg.com/'}, {name: Paper, url: 'https://arxiv.org/abs/1902.00313'}]
tags: ["ICCV"]
short_authors: Liang et al.
---
Relationships encode the interactions among individual instances, and play a
critical role in deep visual scene understanding. Suffering from the high
predictability with non-visual information, existing methods tend to fit the
statistical bias rather than ``learning'' to ``infer'' the relationships from
images. To encourage further development in visual relationships, we propose a
novel method to automatically mine more valuable relationships by pruning
visually-irrelevant ones. We construct a new scene-graph dataset named
Visually-Relevant Relationships Dataset (VrR-VG) based on Visual Genome.
Compared with existing datasets, the performance gap between learnable and
statistical method is more significant in VrR-VG, and frequency-based analysis
does not work anymore. Moreover, we propose to learn a relationship-aware
representation by jointly considering instances, attributes and relationships.
By applying the representation-aware feature learned on VrR-VG, the
performances of image captioning and visual question answering are
systematically improved with a large margin, which demonstrates the gain of our
dataset and the features embedding schema. VrR-VG is available via
http://vrr-vg.com/.