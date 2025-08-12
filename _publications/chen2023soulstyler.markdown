---
layout: publication
title: 'Soulstyler: Using Large Language Model To Guide Image Style Transfer For Target
  Object'
authors: Junhao Chen, Peng Rong, Jingbo Sun, Chao Li, Xiang Li, Hongwu Lv
conference: Arxiv
year: 2023
bibkey: chen2023soulstyler
citations: 0
additional_links: [{name: Code, url: 'https://github.com/yisuanwang/Soulstyler'},
  {name: Paper, url: 'https://arxiv.org/abs/2311.13562'}]
tags: ["Tools & Libraries"]
short_authors: Chen et al.
---
Image style transfer occupies an important place in both computer graphics
and computer vision. However, most current methods require reference to
stylized images and cannot individually stylize specific objects. To overcome
this limitation, we propose the "Soulstyler" framework, which allows users to
guide the stylization of specific objects in an image through simple textual
descriptions. We introduce a large language model to parse the text and
identify stylization goals and specific styles. Combined with a CLIP-based
semantic visual embedding encoder, the model understands and matches text and
image content. We also introduce a novel localized text-image block matching
loss that ensures that style transfer is performed only on specified target
objects, while non-target regions remain in their original style. Experimental
results demonstrate that our model is able to accurately perform style transfer
on target objects according to textual descriptions without affecting the style
of background regions. Our code will be available at
https://github.com/yisuanwang/Soulstyler.