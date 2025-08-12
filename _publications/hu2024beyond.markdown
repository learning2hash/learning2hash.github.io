---
layout: publication
title: 'Beyond Color And Lines: Zero-shot Style-specific Image Variations With Coordinated
  Semantics'
authors: Jinghao Hu, Yuhe Zhang, Guohua Geng, Liuyuxin Yang, Jiarui Yan, Jingtao Cheng,
  Yadong Zhang, Kang Li
conference: Arxiv
year: 2024
bibkey: hu2024beyond
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.18537'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hu et al.
---
Traditionally, style has been primarily considered in terms of artistic
elements such as colors, brushstrokes, and lighting. However, identical
semantic subjects, like people, boats, and houses, can vary significantly
across different artistic traditions, indicating that style also encompasses
the underlying semantics. Therefore, in this study, we propose a zero-shot
scheme for image variation with coordinated semantics. Specifically, our scheme
transforms the image-to-image problem into an image-to-text-to-image problem.
The image-to-text operation employs vision-language models e.g., BLIP) to
generate text describing the content of the input image, including the objects
and their positions. Subsequently, the input style keyword is elaborated into a
detailed description of this style and then merged with the content text using
the reasoning capabilities of ChatGPT. Finally, the text-to-image operation
utilizes a Diffusion model to generate images based on the text prompt. To
enable the Diffusion model to accommodate more styles, we propose a fine-tuning
strategy that injects text and style constraints into cross-attention. This
ensures that the output image exhibits similar semantics in the desired style.
To validate the performance of the proposed scheme, we constructed a benchmark
comprising images of various styles and scenes and introduced two novel
metrics. Despite its simplicity, our scheme yields highly plausible results in
a zero-shot manner, particularly for generating stylized images with
high-fidelity semantics.