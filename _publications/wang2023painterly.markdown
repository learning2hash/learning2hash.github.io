---
layout: publication
title: Painterly Image Harmonization Via Adversarial Residual Learning
authors: Xudong Wang, Li Niu, Junyan Cao, Yan Hong, Liqing Zhang
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: wang2023painterly
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.08646'}]
tags: ["Evaluation", "Robustness"]
short_authors: Wang et al.
---
Image compositing plays a vital role in photo editing. After inserting a
foreground object into another background image, the composite image may look
unnatural and inharmonious. When the foreground is photorealistic and the
background is an artistic painting, painterly image harmonization aims to
transfer the style of background painting to the foreground object, which is a
challenging task due to the large domain gap between foreground and background.
In this work, we employ adversarial learning to bridge the domain gap between
foreground feature map and background feature map. Specifically, we design a
dual-encoder generator, in which the residual encoder produces the residual
features added to the foreground feature map from main encoder. Then, a
pixel-wise discriminator plays against the generator, encouraging the refined
foreground feature map to be indistinguishable from background feature map.
Extensive experiments demonstrate that our method could achieve more harmonious
and visually appealing results than previous methods.