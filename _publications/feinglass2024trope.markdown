---
layout: publication
title: 'TROPE: Training-free Object-part Enhancement For Seamlessly Improving Fine-grained
  Zero-shot Image Captioning'
authors: Joshua Feinglass, Yezhou Yang
conference: Arxiv
year: 2024
bibkey: feinglass2024trope
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.19960'}]
tags: []
short_authors: Joshua Feinglass, Yezhou Yang
---
Zero-shot inference, where pre-trained models perform tasks without specific
training data, is an exciting emergent ability of large models like CLIP.
Although there has been considerable exploration into enhancing zero-shot
abilities in image captioning (IC) for popular datasets such as MSCOCO and
Flickr8k, these approaches fall short with fine-grained datasets like CUB, FLO,
UCM-Captions, and Sydney-Captions. These datasets require captions to discern
between visually and semantically similar classes, focusing on detailed object
parts and their attributes. To overcome this challenge, we introduce
TRaining-Free Object-Part Enhancement (TROPE). TROPE enriches a base caption
with additional object-part details using object detector proposals and Natural
Language Processing techniques. It complements rather than alters the base
caption, allowing seamless integration with other captioning methods and
offering users enhanced flexibility. Our evaluations show that TROPE
consistently boosts performance across all tested zero-shot IC approaches and
achieves state-of-the-art results on fine-grained IC datasets.