---
layout: publication
title: Robust Copy-move Forgery Detection By False Alarms Control
authors: Thibaud Ehret
conference: Arxiv
year: 2019
bibkey: ehret2019robust
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.00649'}]
tags: []
short_authors: Thibaud Ehret
---
Detecting reliably copy-move forgeries is difficult because images do contain
similar objects. The question is: how to discard natural image
self-similarities while still detecting copy-moved parts as being "unnaturally
similar"? Copy-move may have been performed after a rotation, a change of scale
and followed by JPEG compression or the addition of noise. For this reason, we
base our method on SIFT, which provides sparse keypoints with scale, rotation
and illumination invariant descriptors. To discriminate natural descriptor
matches from artificial ones, we introduce an a contrario method which gives
theoretical guarantees on the number of false alarms. We validate our method on
several databases. Being fully unsupervised it can be integrated into any
generic automated image tampering detection pipeline.