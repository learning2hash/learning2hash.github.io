---
layout: publication
title: "Face Retrieval using Frequency Decoded Local Descriptor"
authors: Dubey Shiv Ram
conference: Arxiv
year: 2017
bibkey: dubey2017face
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1709.06508"}
tags: ['ARXIV', 'TIP']
---
The local descriptors have been the backbone of most of the computer vision problems. Most of the existing local descriptors are generated over the raw input images. In order to increase the discriminative power of the local descriptors, some researchers converted the raw image into multiple images with the help of some high and low pass frequency filters, then the local descriptors are computed over each filtered image and finally concatenated into a single descriptor. By doing so, these approaches do not utilize the inter frequency relationship which causes the less improvement in the discriminative power of the descriptor that could be achieved. In this paper, this problem is solved by utilizing the decoder concept of multi-channel decoded local binary pattern over the multi-frequency patterns. A frequency decoded local binary pattern (FDLBP) is proposed with two decoders. Each decoder works with one low frequency pattern and two high frequency patterns. Finally, the descriptors from both decoders are concatenated to form the single descriptor. The face retrieval experiments are conducted over four benchmarks and challenging databases such as PaSC, LFW, PubFig, and ESSEX. The experimental results confirm the superiority of the FDLBP descriptor as compared to the state-of-the-art descriptors such as LBP, SOBEL_LBP, BoF_LBP, SVD_S_LBP, mdLBP, etc.