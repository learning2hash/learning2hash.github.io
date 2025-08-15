---
layout: publication
title: 'Fastbcsd: Fast And Efficient Neural Network For Binary Code Similarity Detection'
authors: Chensen Huang, Guibo Zhu, Guojing Ge, Taihao Li, Jinqiao Wang
conference: Arxiv
year: 2023
bibkey: huang2023fastbcsd
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14168'}]
tags: ["Datasets"]
short_authors: Huang et al.
---
Binary code similarity detection (BCSD) has various applications, including
but not limited to vulnerability detection, plagiarism detection, and malware
detection. Previous research efforts mainly focus on transforming binary code
to assembly code strings using reverse compilation and then using pre-trained
deep learning models with large parameters to obtain feature representation
vector of binary code. While these models have proven to be effective in
representing binary code, their large parameter size leads to considerable
computational expenses during both training and inference. In this paper, we
present a lightweight neural network, called FastBCSD, that employs a dynamic
instruction vector encoding method and takes only assembly code as input
feature to achieve comparable accuracy to the pre-training models while
reducing the computational resources and time cost.
  On the BinaryCorp dataset, our method achieves a similar average MRR score to
the state-of-the-art pre-training-based method (jTrans), while on the
BinaryCorp 3M dataset, our method even outperforms the latest technology by
0.01. Notably, FastBCSD has a much smaller parameter size (13.4M) compared to
jTrans (87.88M), and its latency time is 1/5 of jTrans on NVIDIA GTX 1080Ti.