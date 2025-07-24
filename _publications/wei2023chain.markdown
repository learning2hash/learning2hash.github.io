---
layout: publication
title: 'CHAIN: Exploring Global-local Spatio-temporal Information For Improved Self-supervised
  Video Hashing'
authors: Rukai Wei, Yu Liu, Jingkuan Song, Heng Cui, Yanzhao Xie, Ke Zhou
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: wei2023chain
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.18926'}]
tags: ["Compact Codes", "Datasets", "Evaluation", "Hashing Methods", "Self-Supervised", "Video Retrieval"]
short_authors: Wei et al.
---
Compressing videos into binary codes can improve retrieval speed and reduce
storage overhead. However, learning accurate hash codes for video retrieval can
be challenging due to high local redundancy and complex global dependencies
between video frames, especially in the absence of labels. Existing
self-supervised video hashing methods have been effective in designing
expressive temporal encoders, but have not fully utilized the temporal dynamics
and spatial appearance of videos due to less challenging and unreliable
learning tasks. To address these challenges, we begin by utilizing the
contrastive learning task to capture global spatio-temporal information of
videos for hashing. With the aid of our designed augmentation strategies, which
focus on spatial and temporal variations to create positive pairs, the learning
framework can generate hash codes that are invariant to motion, scale, and
viewpoint. Furthermore, we incorporate two collaborative learning tasks, i.e.,
frame order verification and scene change regularization, to capture local
spatio-temporal details within video frames, thereby enhancing the perception
of temporal structure and the modeling of spatio-temporal relationships. Our
proposed Contrastive Hashing with Global-Local Spatio-temporal Information
(CHAIN) outperforms state-of-the-art self-supervised video hashing methods on
four video benchmark datasets. Our codes will be released.