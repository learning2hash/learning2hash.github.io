---
layout: publication
title: Image Compression With Encoder-decoder Matched Semantic Segmentation
authors: Trinh Man Hoang, Jinjia Zhou, Yibo Fan
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: hoang2020image
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.09642'}]
tags: ["CVPR"]
short_authors: Trinh Man Hoang, Jinjia Zhou, Yibo Fan
---
In recent years, layered image compression is demonstrated to be a promising
direction, which encodes a compact representation of the input image and apply
an up-sampling network to reconstruct the image. To further improve the quality
of the reconstructed image, some works transmit the semantic segment together
with the compressed image data. Consequently, the compression ratio is also
decreased because extra bits are required for transmitting the semantic
segment. To solve this problem, we propose a new layered image compression
framework with encoder-decoder matched semantic segmentation (EDMS). And then,
followed by the semantic segmentation, a special convolution neural network is
used to enhance the inaccurate semantic segment. As a result, the accurate
semantic segment can be obtained in the decoder without requiring extra bits.
The experimental results show that the proposed EDMS framework can get up to
35.31% BD-rate reduction over the HEVC-based (BPG) codec, 5% bitrate, and 24%
encoding time saving compare to the state-of-the-art semantic-based image
codec.