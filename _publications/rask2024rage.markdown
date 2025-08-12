---
layout: publication
title: 'RAGE For The Machine: Image Compression With Low-cost Random Access For Embedded
  Applications'
authors: Christian D. Rask, Daniel E. Lucani
conference: Arxiv
year: 2024
bibkey: rask2024rage
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.05974'}]
tags: []
short_authors: Christian D. Rask, Daniel E. Lucani
---
We introduce RAGE, an image compression framework that achieves four
generally conflicting objectives: 1) good compression for a wide variety of
color images, 2) computationally efficient, fast decompression, 3) fast random
access of images with pixel-level granularity without the need to decompress
the entire image, 4) support for both lossless and lossy compression. To
achieve these, we rely on the recent concept of generalized deduplication (GD),
which is known to provide efficient lossless (de)compression and fast random
access in time-series data, and deliver key expansions suitable for image
compression, both lossless and lossy. Using nine different datasets, incl.
graphics, logos, natural images, we show that RAGE has similar or better
compression ratios to state-of-the-art lossless image compressors, while
delivering pixel-level random access capabilities. Tests in an ARM Cortex-M33
platform show seek times between 9.9 and 40.6~ns and average decoding time per
pixel between 274 and 1226~ns. Our measurements also show that RAGE's lossy
variant, RAGE-Q, outperforms JPEG by several fold in terms of distortion in
embedded graphics and has reasonable compression and distortion for natural
images.