---
layout: publication
title: Deep Hashing With Hash-consistent Large Margin Proxy Embeddings
authors: Pedro Morgado, Yunsheng Li, Jose Costa Pereira, Mohammad Saberian, Nuno Vasconcelos
conference: Arxiv
year: 2020
citations: 6
bibkey: morgado2020deep
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.13912'}]
tags: [Hashing Methods, Deep Hashing, Efficient Learning, Evaluation Metrics]
---
Image hash codes are produced by binarizing the embeddings of convolutional
neural networks (CNN) trained for either classification or retrieval. While
proxy embeddings achieve good performance on both tasks, they are non-trivial
to binarize, due to a rotational ambiguity that encourages non-binary
embeddings. The use of a fixed set of proxies (weights of the CNN
classification layer) is proposed to eliminate this ambiguity, and a procedure
to design proxy sets that are nearly optimal for both classification and
hashing is introduced. The resulting hash-consistent large margin (HCLM)
proxies are shown to encourage saturation of hashing units, thus guaranteeing a
small binarization error, while producing highly discriminative hash-codes. A
semantic extension (sHCLM), aimed to improve hashing performance in a transfer
scenario, is also proposed. Extensive experiments show that sHCLM embeddings
achieve significant improvements over state-of-the-art hashing procedures on
several small and large datasets, both within and beyond the set of training
classes.