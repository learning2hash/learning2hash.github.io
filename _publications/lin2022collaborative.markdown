---
layout: publication
title: Collaborative Neural Rendering Using Anime Character Sheets
authors: Zuzeng Lin, Ailin Huang, Zhewei Huang
conference: Proceedings of the Thirty-Second International Joint Conference on Artificial
  Intelligence
year: 2023
bibkey: lin2022collaborative
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05378'}]
tags: ["Datasets"]
short_authors: Zuzeng Lin, Ailin Huang, Zhewei Huang
---
Drawing images of characters with desired poses is an essential but laborious
task in anime production. Assisting artists to create is a research hotspot in
recent years. In this paper, we present the Collaborative Neural Rendering
(CoNR) method, which creates new images for specified poses from a few
reference images (AKA Character Sheets). In general, the diverse hairstyles and
garments of anime characters defies the employment of universal body models
like SMPL, which fits in most nude human shapes. To overcome this, CoNR uses a
compact and easy-to-obtain landmark encoding to avoid creating a unified UV
mapping in the pipeline. In addition, the performance of CoNR can be
significantly improved when referring to multiple reference images, thanks to
feature space cross-view warping in a carefully designed neural network.
Moreover, we have collected a character sheet dataset containing over 700,000
hand-drawn and synthesized images of diverse poses to facilitate research in
this area. Our code and demo are available at
https://github.com/megvii-research/IJCAI2023-CoNR.