---
layout: publication
title: 'Autossvh: Exploring Automated Frame Sampling For Efficient Self-supervised
  Video Hashing'
authors: Niu Lian, Jun Li, Jinpeng Wang, Ruisheng Luo, Yaowei Wang, Shu-Tao Xia, Bin
  Chen
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: lian2025autossvh
citations: 0
additional_links: [{name: Code, url: 'https://github.com/EliSpectre/CVPR25-AutoSSVH'},
  {name: Paper, url: 'https://arxiv.org/abs/2504.03587'}]
tags: ["CVPR", "Efficiency", "Hashing Methods", "Robustness", "Self-Supervised", "Supervised", "Tools & Libraries"]
short_authors: Lian et al.
---
Self-Supervised Video Hashing (SSVH) compresses videos into hash codes for
efficient indexing and retrieval using unlabeled training videos. Existing
approaches rely on random frame sampling to learn video features and treat all
frames equally. This results in suboptimal hash codes, as it ignores
frame-specific information density and reconstruction difficulty. To address
this limitation, we propose a new framework, termed AutoSSVH, that employs
adversarial frame sampling with hash-based contrastive learning. Our
adversarial sampling strategy automatically identifies and selects challenging
frames with richer information for reconstruction, enhancing encoding
capability. Additionally, we introduce a hash component voting strategy and a
point-to-set (P2Set) hash-based contrastive objective, which help capture
complex inter-video semantic relationships in the Hamming space and improve the
discriminability of learned hash codes. Extensive experiments demonstrate that
AutoSSVH achieves superior retrieval efficacy and efficiency compared to
state-of-the-art approaches. Code is available at
https://github.com/EliSpectre/CVPR25-AutoSSVH.