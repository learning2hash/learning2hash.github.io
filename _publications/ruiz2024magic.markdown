---
layout: publication
title: 'Magic Insert: Style-aware Drag-and-drop'
authors: Nataniel Ruiz, Yuanzhen Li, Neal Wadhwa, Yael Pritch, Michael Rubinstein,
  David E. Jacobs, Shlomi Fruchter
conference: Arxiv
year: 2024
bibkey: ruiz2024magic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.02489'}]
tags: []
short_authors: Ruiz et al.
---
We present Magic Insert, a method for dragging-and-dropping subjects from a
user-provided image into a target image of a different style in a physically
plausible manner while matching the style of the target image. This work
formalizes the problem of style-aware drag-and-drop and presents a method for
tackling it by addressing two sub-problems: style-aware personalization and
realistic object insertion in stylized images. For style-aware personalization,
our method first fine-tunes a pretrained text-to-image diffusion model using
LoRA and learned text tokens on the subject image, and then infuses it with a
CLIP representation of the target style. For object insertion, we use
Bootstrapped Domain Adaption to adapt a domain-specific photorealistic object
insertion model to the domain of diverse artistic styles. Overall, the method
significantly outperforms traditional approaches such as inpainting. Finally,
we present a dataset, SubjectPlop, to facilitate evaluation and future progress
in this area. Project page: https://magicinsert.github.io/