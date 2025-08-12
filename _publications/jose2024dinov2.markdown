---
layout: publication
title: 'Dinov2 Meets Text: A Unified Framework For Image- And Pixel-level Vision-language
  Alignment'
authors: "Cijo Jose, Th\xE9o Moutakanni, Dahyun Kang, Federico Baldassarre, Timoth\xE9\
  e Darcet, Hu Xu, Daniel Li, Marc Szafraniec, Micha\xEBl Ramamonjisoa, Maxime Oquab,\
  \ Oriane Sim\xE9oni, Huy V. Vo, Patrick Labatut, Piotr Bojanowski"
conference: Arxiv
year: 2024
bibkey: jose2024dinov2
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.16334'}]
tags: []
short_authors: Jose et al.
---
Self-supervised visual foundation models produce powerful embeddings that
achieve remarkable performance on a wide range of downstream tasks. However,
unlike vision-language models such as CLIP, self-supervised visual features are
not readily aligned with language, hindering their adoption in open-vocabulary
tasks. Our method, named dino.txt, unlocks this new ability for DINOv2, a
widely used self-supervised visual encoder. We build upon the LiT training
strategy, which trains a text encoder to align with a frozen vision model but
leads to unsatisfactory results on dense tasks. We propose several key
ingredients to improve performance on both global and dense tasks, such as
concatenating the [CLS] token with the patch average to train the alignment and
curating data using both text and image modalities. With these, we successfully
train a CLIP-like model with only a fraction of the computational cost compared
to CLIP while achieving state-of-the-art results in zero-shot classification
and open-vocabulary semantic segmentation.