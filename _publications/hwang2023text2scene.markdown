---
layout: publication
title: 'Text2scene: Text-driven Indoor Scene Stylization With Part-aware Details'
authors: Inwoo Hwang, Hyeonwoo Kim, Young Min Kim
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: hwang2023text2scene
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.16880'}]
tags: ["CVPR"]
short_authors: Inwoo Hwang, Hyeonwoo Kim, Young Min Kim
---
We propose Text2Scene, a method to automatically create realistic textures
for virtual scenes composed of multiple objects. Guided by a reference image
and text descriptions, our pipeline adds detailed texture on labeled 3D
geometries in the room such that the generated colors respect the hierarchical
structure or semantic parts that are often composed of similar materials.
Instead of applying flat stylization on the entire scene at a single step, we
obtain weak semantic cues from geometric segmentation, which are further
clarified by assigning initial colors to segmented parts. Then we add texture
details for individual objects such that their projections on image space
exhibit feature embedding aligned with the embedding of the input. The
decomposition makes the entire pipeline tractable to a moderate amount of
computation resources and memory. As our framework utilizes the existing
resources of image and text embedding, it does not require dedicated datasets
with high-quality textures designed by skillful artists. To the best of our
knowledge, it is the first practical and scalable approach that can create
detailed and realistic textures of the desired style that maintain structural
context for scenes with multiple objects.