---
layout: publication
title: Nearest-neighbor Inter-intra Contrastive Learning From Unlabeled Videos
authors: David Fan, Deyu Yang, Xinyu Li, Vimal Bhat, Rohith Mv
conference: Arxiv
year: 2023
bibkey: fan2023nearest
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.07317'}]
tags: ["Self-Supervised", "Video Retrieval"]
short_authors: Fan et al.
---
Contrastive learning has recently narrowed the gap between self-supervised
and supervised methods in image and video domain. State-of-the-art video
contrastive learning methods such as CVRL and \(\rho\)-MoCo spatiotemporally
augment two clips from the same video as positives. By only sampling positive
clips locally from a single video, these methods neglect other semantically
related videos that can also be useful. To address this limitation, we leverage
nearest-neighbor videos from the global space as additional positive pairs,
thus improving positive key diversity and introducing a more relaxed notion of
similarity that extends beyond video and even class boundaries. Our method,
Inter-Intra Video Contrastive Learning (IIVCL), improves performance on a range
of video tasks.