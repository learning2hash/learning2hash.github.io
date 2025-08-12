---
layout: publication
title: Online Deep Clustering With Video Track Consistency
authors: Alessandra Alfani, Federico Becattini, Lorenzo Seidenari, Alberto del Bimbo
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: alfani2022online
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.03086'}]
tags: []
short_authors: Alfani et al.
---
Several unsupervised and self-supervised approaches have been developed in
recent years to learn visual features from large-scale unlabeled datasets.
Their main drawback however is that these methods are hardly able to recognize
visual features of the same object if it is simply rotated or the perspective
of the camera changes. To overcome this limitation and at the same time exploit
a useful source of supervision, we take into account video object tracks.
Following the intuition that two patches in a track should have similar visual
representations in a learned feature space, we adopt an unsupervised
clustering-based approach and constrain such representations to be labeled as
the same category since they likely belong to the same object or object part.
Experimental results on two downstream tasks on different datasets demonstrate
the effectiveness of our Online Deep Clustering with Video Track Consistency
(ODCT) approach compared to prior work, which did not leverage temporal
information. In addition we show that exploiting an unsupervised
class-agnostic, yet noisy, track generator yields to better accuracy compared
to relying on costly and precise track annotations.