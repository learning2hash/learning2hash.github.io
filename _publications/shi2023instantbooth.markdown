---
layout: publication
title: 'Instantbooth: Personalized Text-to-image Generation Without Test-time Finetuning'
authors: Jing Shi, Wei Xiong, Zhe Lin, Hyun Joon Jung
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: shi2023instantbooth
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03411'}]
tags: ["CVPR"]
short_authors: Shi et al.
---
Recent advances in personalized image generation allow a pre-trained
text-to-image model to learn a new concept from a set of images. However,
existing personalization approaches usually require heavy test-time finetuning
for each concept, which is time-consuming and difficult to scale. We propose
InstantBooth, a novel approach built upon pre-trained text-to-image models that
enables instant text-guided image personalization without any test-time
finetuning. We achieve this with several major components. First, we learn the
general concept of the input images by converting them to a textual token with
a learnable image encoder. Second, to keep the fine details of the identity, we
learn rich visual feature representation by introducing a few adapter layers to
the pre-trained model. We train our components only on text-image pairs without
using paired images of the same concept. Compared to test-time finetuning-based
methods like DreamBooth and Textual-Inversion, our model can generate
competitive results on unseen concepts concerning language-image alignment,
image fidelity, and identity preservation while being 100 times faster.