---
layout: publication
title: Region-based Representations Revisited
authors: Michal Shlapentokh-rothman, Ansel Blume, Yao Xiao, Yuqun Wu, Sethuraman T,
  Heyi Tao, Jae Yong Lee, Wilfredo Torres, Yu-xiong Wang, Derek Hoiem
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: shlapentokhrothman2024region
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.02352'}]
tags: ["CVPR"]
short_authors: Shlapentokh-rothman et al.
---
We investigate whether region-based representations are effective for
recognition. Regions were once a mainstay in recognition approaches, but pixel
and patch-based features are now used almost exclusively. We show that recent
class-agnostic segmenters like SAM can be effectively combined with strong
unsupervised representations like DINOv2 and used for a wide variety of tasks,
including semantic segmentation, object-based image retrieval, and multi-image
analysis. Once the masks and features are extracted, these representations,
even with linear decoders, enable competitive performance, making them well
suited to applications that require custom queries. The compactness of the
representation also makes it well-suited to video analysis and other problems
requiring inference across many images.