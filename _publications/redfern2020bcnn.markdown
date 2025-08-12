---
layout: publication
title: 'BCNN: A Binary CNN With All Matrix Ops Quantized To 1 Bit Precision'
authors: Arthur J. Redfern, Lijun Zhu, Molly K. Newquist
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: redfern2020bcnn
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.00704'}]
tags: ["CVPR"]
short_authors: Arthur J. Redfern, Lijun Zhu, Molly K. Newquist
---
This paper describes a CNN where all CNN style 2D convolution operations that
lower to matrix matrix multiplication are fully binary. The network is derived
from a common building block structure that is consistent with a constructive
proof outline showing that binary neural networks are universal function
approximators. 71.24% top 1 accuracy on the 2012 ImageNet validation set was
achieved with a 2 step training procedure and implementation strategies
optimized for binary operands are provided.