---
layout: publication
title: Lightweight Image Codec Via Multi-grid Multi-block-size Vector Quantization
  (MGBVQ)
authors: Yifan Wang, Zhanxuan Mei, Ioannis Katsavounidis, C. -C. Jay Kuo
conference: Arxiv
year: 2022
bibkey: wang2022lightweight
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.12139'}]
tags: ["Quantization"]
short_authors: Wang et al.
---
A multi-grid multi-block-size vector quantization (MGBVQ) method is proposed
for image coding in this work. The fundamental idea of image coding is to
remove correlations among pixels before quantization and entropy coding, e.g.,
the discrete cosine transform (DCT) and intra predictions, adopted by modern
image coding standards. We present a new method to remove pixel correlations.
First, by decomposing correlations into long- and short-range correlations, we
represent long-range correlations in coarser grids due to their smoothness,
thus leading to a multi-grid (MG) coding architecture. Second, we show that
short-range correlations can be effectively coded by a suite of vector
quantizers (VQs). Along this line, we argue the effectiveness of VQs of very
large block sizes and present a convenient way to implement them. It is shown
by experimental results that MGBVQ offers excellent rate-distortion (RD)
performance, which is comparable with existing image coders, at much lower
complexity. Besides, it provides a progressive coded bitstream.