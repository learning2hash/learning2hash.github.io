---
layout: publication
title: Neural Multi-scale Image Compression
authors: Ken Nakanishi, Shin-ichi Maeda, Takeru Miyato, Daisuke Okanohara
conference: Lecture Notes in Computer Science
year: 2019
bibkey: nakanishi2018neural
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.06386'}]
tags: []
short_authors: Nakanishi et al.
---
This study presents a new lossy image compression method that utilizes the
multi-scale features of natural images. Our model consists of two networks:
multi-scale lossy autoencoder and parallel multi-scale lossless coder. The
multi-scale lossy autoencoder extracts the multi-scale image features to
quantized variables and the parallel multi-scale lossless coder enables rapid
and accurate lossless coding of the quantized variables via encoding/decoding
the variables in parallel. Our proposed model achieves comparable performance
to the state-of-the-art model on Kodak and RAISE-1k dataset images, and it
encodes a PNG image of size \\(768 \times 512\\) in 70 ms with a single GPU and a
single CPU process and decodes it into a high-fidelity image in approximately
200 ms.