---
layout: publication
title: 'Learning The Ropes: Better 2D And 3D Position Encodings With STRING'
authors: "Connor Schenck, Isaac Reid, Mithun George Jacob, Alex Bewley, Joshua Ainslie,\
  \ David Rendleman, Deepali Jain, Mohit Sharma, Avinava Dubey, Ayzaan Wahid, Sumeet\
  \ Singh, Ren\xE9 Wagner, Tianli Ding, Chuyuan Fu, Arunkumar Byravan, Jake Varley,\
  \ Alexey Gritsenko, Matthias Minderer, Dmitry Kalashnikov, Jonathan Tompson, Vikas\
  \ Sindhwani, Krzysztof Choromanski"
conference: Arxiv
year: 2025
bibkey: schenck2025learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.02562'}]
tags: []
short_authors: Schenck et al.
---
We introduce STRING: Separable Translationally Invariant Position Encodings.
STRING extends Rotary Position Encodings, a recently proposed and widely used
algorithm in large language models, via a unifying theoretical framework.
Importantly, STRING still provides exact translation invariance, including
token coordinates of arbitrary dimensionality, whilst maintaining a low
computational footprint. These properties are especially important in robotics,
where efficient 3D token representation is key. We integrate STRING into Vision
Transformers with RGB(-D) inputs (color plus optional depth), showing
substantial gains, e.g. in open-vocabulary object detection and for robotics
controllers. We complement our experiments with a rigorous mathematical
analysis, proving the universality of our methods.