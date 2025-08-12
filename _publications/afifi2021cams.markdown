---
layout: publication
title: 'CAMS: Color-aware Multi-style Transfer'
authors: Mahmoud Afifi, Abdullah Abuolaim, Mostafa Hussien, Marcus A. Brubaker, Michael
  S. Brown
conference: Arxiv
year: 2021
bibkey: afifi2021cams
citations: 2
additional_links: [{name: Code, url: 'https://github.com/mahmoudnafifi/color-aware-style-transfer'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.13920'}]
tags: []
short_authors: Afifi et al.
---
Image style transfer aims to manipulate the appearance of a source image, or
"content" image, to share similar texture and colors of a target "style" image.
Ideally, the style transfer manipulation should also preserve the semantic
content of the source image. A commonly used approach to assist in transferring
styles is based on Gram matrix optimization. One problem of Gram matrix-based
optimization is that it does not consider the correlation between colors and
their styles. Specifically, certain textures or structures should be associated
with specific colors. This is particularly challenging when the target style
image exhibits multiple style types. In this work, we propose a color-aware
multi-style transfer method that generates aesthetically pleasing results while
preserving the style-color correlation between style and generated images. We
achieve this desired outcome by introducing a simple but efficient modification
to classic Gram matrix-based style transfer optimization. A nice feature of our
method is that it enables the users to manually select the color associations
between the target style and content image for more transfer flexibility. We
validated our method with several qualitative comparisons, including a user
study conducted with 30 participants. In comparison with prior work, our method
is simple, easy to implement, and achieves visually appealing results when
targeting images that have multiple styles. Source code is available at
https://github.com/mahmoudnafifi/color-aware-style-transfer.