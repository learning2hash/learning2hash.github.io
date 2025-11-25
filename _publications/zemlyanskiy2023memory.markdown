---
layout: publication
title: 'MEMORY-VQ: Compression For Tractable Internet-scale Memory'
authors: "Yury Zemlyanskiy, Michiel de Jong, Luke Vilnis, Santiago Onta\xF1\xF3n,\
  \ William W. Cohen, Sumit Sanghai, Joshua Ainslie"
conference: Arxiv
year: 2023
bibkey: zemlyanskiy2023memory
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.14903'}]
tags: ["Memory Efficiency", "Quantization"]
short_authors: Zemlyanskiy et al.
---
Retrieval augmentation is a powerful but expensive method to make language
models more knowledgeable about the world. Memory-based methods like LUMEN
pre-compute token representations for retrieved passages to drastically speed
up inference. However, memory also leads to much greater storage requirements
from storing pre-computed representations.
  We propose MEMORY-VQ, a new method to reduce storage requirements of
memory-augmented models without sacrificing performance. Our method uses a
vector quantization variational autoencoder (VQ-VAE) to compress token
representations. We apply MEMORY-VQ to the LUMEN model to obtain LUMEN-VQ, a
memory model that achieves a 16x compression rate with comparable performance
on the KILT benchmark. LUMEN-VQ enables practical retrieval augmentation even
for extremely large retrieval corpora.