---
layout: publication
title: Coloristanet For Photorealistic Video Style Transfer
authors: Xiaowen Qiu, Ruize Xu, Boan He, Yingtao Zhang, Wenqiang Zhang, Weifeng Ge
conference: Arxiv
year: 2022
bibkey: qiu2022coloristanet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.09247'}]
tags: []
short_authors: Qiu et al.
---
Photorealistic style transfer aims to transfer the artistic style of an image
onto an input image or video while keeping photorealism. In this paper, we
think it's the summary statistics matching scheme in existing algorithms that
leads to unrealistic stylization. To avoid employing the popular Gram loss, we
propose a self-supervised style transfer framework, which contains a style
removal part and a style restoration part. The style removal network removes
the original image styles, and the style restoration network recovers image
styles in a supervised manner. Meanwhile, to address the problems in current
feature transformation methods, we propose decoupled instance normalization to
decompose feature transformation into style whitening and restylization. It
works quite well in ColoristaNet and can transfer image styles efficiently
while keeping photorealism. To ensure temporal coherency, we also incorporate
optical flow methods and ConvLSTM to embed contextual information. Experiments
demonstrates that ColoristaNet can achieve better stylization effects when
compared with state-of-the-art algorithms.