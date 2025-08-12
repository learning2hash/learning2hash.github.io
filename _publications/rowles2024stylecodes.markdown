---
layout: publication
title: 'Stylecodes: Encoding Stylistic Information For Image Generation'
authors: Ciara Rowles
conference: Arxiv
year: 2024
bibkey: rowles2024stylecodes
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12811'}]
tags: ["Image Retrieval"]
short_authors: Ciara Rowles
---
Diffusion models excel in image generation, but controlling them remains a
challenge. We focus on the problem of style-conditioned image generation.
Although example images work, they are cumbersome: srefs (style-reference
codes) from MidJourney solve this issue by expressing a specific image style in
a short numeric code. These have seen widespread adoption throughout social
media due to both their ease of sharing and the fact they allow using an image
for style control, without having to post the source images themselves.
However, users are not able to generate srefs from their own images, nor is the
underlying training procedure public. We propose StyleCodes: an open-source and
open-research style encoder architecture and training procedure to express
image style as a 20-symbol base64 code. Our experiments show that our encoding
results in minimal loss in quality compared to traditional image-to-style
techniques.