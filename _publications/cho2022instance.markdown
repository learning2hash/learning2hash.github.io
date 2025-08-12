---
layout: publication
title: Instance-aware Image Completion
authors: Jinoh Cho, Minguk Kang, Vibhav Vineet, Jaesik Park
conference: Arxiv
year: 2022
bibkey: cho2022instance
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.12350'}]
tags: []
short_authors: Cho et al.
---
Image completion is a task that aims to fill in the missing region of a
masked image with plausible contents. However, existing image completion
methods tend to fill in the missing region with the surrounding texture instead
of hallucinating a visual instance that is suitable in accordance with the
context of the scene. In this work, we propose a novel image completion model,
dubbed ImComplete, that hallucinates the missing instance that harmonizes well
with - and thus preserves - the original context. ImComplete first adopts a
transformer architecture that considers the visible instances and the location
of the missing region. Then, ImComplete completes the semantic segmentation
masks within the missing region, providing pixel-level semantic and structural
guidance. Finally, the image synthesis blocks generate photo-realistic content.
We perform a comprehensive evaluation of the results in terms of visual quality
(LPIPS and FID) and contextual preservation scores (CLIPscore and object
detection accuracy) with COCO-panoptic and Visual Genome datasets. Experimental
results show the superiority of ImComplete on various natural images.