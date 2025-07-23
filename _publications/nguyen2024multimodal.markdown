---
layout: publication
title: Multimodal Learned Sparse Retrieval With Probabilistic Expansion Control
authors: Nguyen Thong, Hendriksen Mariya, Yates Andrew, de Rijke Maarten
conference: Arxiv
year: 2024
bibkey: nguyen2024multimodal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17535'}]
tags: ["Efficiency", "Image Retrieval", "Large-Scale Search", "Multimodal Retrieval", "Similarity Search", "Text Retrieval"]
short_authors: Nguyen et al.
---
Learned sparse retrieval (LSR) is a family of neural methods that encode
queries and documents into sparse lexical vectors that can be indexed and
retrieved efficiently with an inverted index. We explore the application of LSR
to the multi-modal domain, with a focus on text-image retrieval. While LSR has
seen success in text retrieval, its application in multimodal retrieval remains
underexplored. Current approaches like LexLIP and STAIR require complex
multi-step training on massive datasets. Our proposed approach efficiently
transforms dense vectors from a frozen dense model into sparse lexical vectors.
We address issues of high dimension co-activation and semantic deviation
through a new training algorithm, using Bernoulli random variables to control
query expansion. Experiments with two dense models (BLIP, ALBEF) and two
datasets (MSCOCO, Flickr30k) show that our proposed algorithm effectively
reduces co-activation and semantic deviation. Our best-performing sparsified
model outperforms state-of-the-art text-image LSR models with a shorter
training time and lower GPU memory requirements. Our approach offers an
effective solution for training LSR retrieval models in multimodal settings.
Our code and model checkpoints are available at
github.com/thongnt99/lsr-multimodal