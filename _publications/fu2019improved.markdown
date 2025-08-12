---
layout: publication
title: Improved Hybrid Layered Image Compression Using Deep Learning And Traditional
  Codecs
authors: Haisheng Fu, Feng Liang, Bo Lei, Nai Bian, Qian Zhang, Mohammad Akbari, Jie
  Liang, Chengjie Tu
conference: 'Signal Processing: Image Communication'
year: 2020
bibkey: fu2019improved
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.06566'}]
tags: []
short_authors: Fu et al.
---
Recently deep learning-based methods have been applied in image compression
and achieved many promising results. In this paper, we propose an improved
hybrid layered image compression framework by combining deep learning and the
traditional image codecs. At the encoder, we first use a convolutional neural
network (CNN) to obtain a compact representation of the input image, which is
losslessly encoded by the FLIF codec as the base layer of the bit stream. A
coarse reconstruction of the input is obtained by another CNN from the
reconstructed compact representation. The residual between the input and the
coarse reconstruction is then obtained and encoded by the H.265/HEVC-based BPG
codec as the enhancement layer of the bit stream. Experimental results using
the Kodak and Tecnick datasets show that the proposed scheme outperforms the
state-of-the-art deep learning-based layered coding scheme and traditional
codecs including BPG in both PSNR and MS-SSIM metrics across a wide range of
bit rates, when the images are coded in the RGB444 domain.