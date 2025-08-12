---
layout: publication
title: 'Mslkanet: A Multi-scale Large Kernel Attention Network For Scene Text Removal'
authors: Guangtao Lyu
conference: Arxiv
year: 2022
bibkey: lyu2022mslkanet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.06565'}]
tags: []
short_authors: Guangtao Lyu
---
Scene text removal aims to remove the text and fill the regions with
perceptually plausible background information in natural images. It has
attracted increasing attention due to its various applications in privacy
protection, scene text retrieval, and text editing. With the development of
deep learning, the previous methods have achieved significant improvements.
However, most of the existing methods seem to ignore the large perceptive
fields and global information. The pioneer method can get significant
improvements by only changing training data from the cropped image to the full
image. In this paper, we present a single-stage multi-scale network MSLKANet
for scene text removal in full images. For obtaining large perceptive fields
and global information, we propose multi-scale large kernel attention (MSLKA)
to obtain long-range dependencies between the text regions and the backgrounds
at various granularity levels. Furthermore, we combine the large kernel
decomposition mechanism and atrous spatial pyramid pooling to build a large
kernel spatial pyramid pooling (LKSPP), which can perceive more valid pixels in
the spatial dimension while maintaining large receptive fields and low cost of
computation. Extensive experimental results indicate that the proposed method
achieves state-of-the-art performance on both synthetic and real-world datasets
and the effectiveness of the proposed components MSLKA and LKSPP.