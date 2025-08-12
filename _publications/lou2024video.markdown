---
layout: publication
title: Video Inpainting Localization With Contrastive Learning
authors: Zijie Lou, Gang Cao, Man Lin
conference: IEEE Signal Processing Letters
year: 2025
bibkey: lou2024video
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.17628'}]
tags: []
short_authors: Zijie Lou, Gang Cao, Man Lin
---
Deep video inpainting is typically used as malicious manipulation to remove
important objects for creating fake videos. It is significant to identify the
inpainted regions blindly. This letter proposes a simple yet effective forensic
scheme for Video Inpainting LOcalization with ContrAstive Learning (ViLocal).
Specifically, a 3D Uniformer encoder is applied to the video noise residual for
learning effective spatiotemporal forensic features. To enhance the
discriminative power, supervised contrastive learning is adopted to capture the
local inconsistency of inpainted videos through attracting/repelling the
positive/negative pristine and forged pixel pairs. A pixel-wise inpainting
localization map is yielded by a lightweight convolution decoder with a
specialized two-stage training strategy. To prepare enough training samples, we
build a video object segmentation dataset of 2500 videos with pixel-level
annotations per frame. Extensive experimental results validate the superiority
of ViLocal over state-of-the-arts. Code and dataset will be available at
https://github.com/multimediaFor/ViLocal.