---
layout: publication
title: 'FAST: Faster Arbitrarily-shaped Text Detector With Minimalist Kernel Representation'
authors: Zhe Chen, Jiahao Wang, Wenhai Wang, Guo Chen, Enze Xie, Ping Luo, Tong Lu
conference: Arxiv
year: 2021
bibkey: chen2021fast
citations: 5
additional_links: [{name: Code, url: 'https://github.com/czczup/FAST'}, {name: Paper,
    url: 'https://arxiv.org/abs/2111.02394'}]
tags: ["Efficiency"]
short_authors: Chen et al.
---
We propose an accurate and efficient scene text detection framework, termed
FAST (i.e., faster arbitrarily-shaped text detector). Different from recent
advanced text detectors that used complicated post-processing and hand-crafted
network architectures, resulting in low inference speed, FAST has two new
designs. (1) We design a minimalist kernel representation (only has 1-channel
output) to model text with arbitrary shape, as well as a GPU-parallel
post-processing to efficiently assemble text lines with a negligible time
overhead. (2) We search the network architecture tailored for text detection,
leading to more powerful features than most networks that are searched for
image classification. Benefiting from these two designs, FAST achieves an
excellent trade-off between accuracy and efficiency on several challenging
datasets, including Total Text, CTW1500, ICDAR 2015, and MSRA-TD500. For
example, FAST-T yields 81.6% F-measure at 152 FPS on Total-Text, outperforming
the previous fastest method by 1.7 points and 70 FPS in terms of accuracy and
speed. With TensorRT optimization, the inference speed can be further
accelerated to over 600 FPS. Code and models will be released at
https://github.com/czczup/FAST.