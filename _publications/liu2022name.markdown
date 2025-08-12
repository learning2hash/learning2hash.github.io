---
layout: publication
title: 'Name Your Style: An Arbitrary Artist-aware Image Style Transfer'
authors: Zhi-Song Liu, Li-Wen Wang, Wan-Chi Siu, Vicky Kalogeiton
conference: Arxiv
year: 2022
bibkey: liu2022name
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.13562'}]
tags: ["Image Retrieval"]
short_authors: Liu et al.
---
Image style transfer has attracted widespread attention in the past few
years. Despite its remarkable results, it requires additional style images
available as references, making it less flexible and inconvenient. Using text
is the most natural way to describe the style. More importantly, text can
describe implicit abstract styles, like styles of specific artists or art
movements. In this paper, we propose a text-driven image style transfer (TxST)
that leverages advanced image-text encoders to control arbitrary style
transfer. We introduce a contrastive training strategy to effectively extract
style descriptions from the image-text model (i.e., CLIP), which aligns
stylization with the text description. To this end, we also propose a novel and
efficient attention module that explores cross-attentions to fuse style and
content features. Finally, we achieve an arbitrary artist-aware image style
transfer to learn and transfer specific artistic characters such as Picasso,
oil painting, or a rough sketch. Extensive experiments demonstrate that our
approach outperforms the state-of-the-art methods on both image and textual
styles. Moreover, it can mimic the styles of one or many artists to achieve
attractive results, thus highlighting a promising direction in image style
transfer.