---
layout: publication
title: 'Stylebooth: Image Style Editing With Multimodal Instruction'
authors: Zhen Han, Chaojie Mao, Zeyinzi Jiang, Yulin Pan, Jingfeng Zhang
conference: Arxiv
year: 2024
bibkey: han2024stylebooth
citations: 0
additional_links: [{name: Code, url: 'https://ali-vilab.github.io/stylebooth-page/'},
  {name: Paper, url: 'https://arxiv.org/abs/2404.12154'}]
tags: ["Tools & Libraries"]
short_authors: Han et al.
---
Given an original image, image editing aims to generate an image that align
with the provided instruction. The challenges are to accept multimodal inputs
as instructions and a scarcity of high-quality training data, including crucial
triplets of source/target image pairs and multimodal (text and image)
instructions. In this paper, we focus on image style editing and present
StyleBooth, a method that proposes a comprehensive framework for image editing
and a feasible strategy for building a high-quality style editing dataset. We
integrate encoded textual instruction and image exemplar as a unified condition
for diffusion model, enabling the editing of original image following
multimodal instructions. Furthermore, by iterative style-destyle tuning and
editing and usability filtering, the StyleBooth dataset provides
content-consistent stylized/plain image pairs in various categories of styles.
To show the flexibility of StyleBooth, we conduct experiments on diverse tasks,
such as text-based style editing, exemplar-based style editing and
compositional style editing. The results demonstrate that the quality and
variety of training data significantly enhance the ability to preserve content
and improve the overall quality of generated images in editing tasks. Project
page can be found at https://ali-vilab.github.io/stylebooth-page/.