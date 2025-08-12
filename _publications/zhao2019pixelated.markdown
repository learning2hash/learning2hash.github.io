---
layout: publication
title: Pixelated Semantic Colorization
authors: Jiaojiao Zhao, Jungong Han, Ling Shao, Cees G. M. Snoek
conference: International Journal of Computer Vision
year: 2019
bibkey: zhao2019pixelated
citations: 77
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.10889'}]
tags: []
short_authors: Zhao et al.
---
While many image colorization algorithms have recently shown the capability
of producing plausible color versions from gray-scale photographs, they still
suffer from limited semantic understanding. To address this shortcoming, we
propose to exploit pixelated object semantics to guide image colorization. The
rationale is that human beings perceive and distinguish colors based on the
semantic categories of objects. Starting from an autoregressive model, we
generate image color distributions, from which diverse colored results are
sampled. We propose two ways to incorporate object semantics into the
colorization model: through a pixelated semantic embedding and a pixelated
semantic generator. Specifically, the proposed convolutional neural network
includes two branches. One branch learns what the object is, while the other
branch learns the object colors. The network jointly optimizes a color
embedding loss, a semantic segmentation loss and a color generation loss, in an
end-to-end fashion. Experiments on PASCAL VOC2012 and COCO-stuff reveal that
our network, when trained with semantic segmentation labels, produces more
realistic and finer results compared to the colorization state-of-the-art.