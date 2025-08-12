---
layout: publication
title: 'Matchu: Matching Unseen Objects For 6D Pose Estimation From RGB-D Images'
authors: Junwen Huang, Hao Yu, Kuan-Ting Yu, Nassir Navab, Slobodan Ilic, Benjamin
  Busam
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: huang2024matchu
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.01517'}]
tags: ["CVPR"]
short_authors: Huang et al.
---
Recent learning methods for object pose estimation require resource-intensive
training for each individual object instance or category, hampering their
scalability in real applications when confronted with previously unseen
objects. In this paper, we propose MatchU, a Fuse-Describe-Match strategy for
6D pose estimation from RGB-D images. MatchU is a generic approach that fuses
2D texture and 3D geometric cues for 6D pose prediction of unseen objects. We
rely on learning geometric 3D descriptors that are rotation-invariant by
design. By encoding pose-agnostic geometry, the learned descriptors naturally
generalize to unseen objects and capture symmetries. To tackle ambiguous
associations using 3D geometry only, we fuse additional RGB information into
our descriptor. This is achieved through a novel attention-based mechanism that
fuses cross-modal information, together with a matching loss that leverages the
latent space learned from RGB data to guide the descriptor learning process.
Extensive experiments reveal the generalizability of both the RGB-D fusion
strategy as well as the descriptor efficacy. Benefiting from the novel designs,
MatchU surpasses all existing methods by a significant margin in terms of both
accuracy and speed, even without the requirement of expensive re-training or
rendering.