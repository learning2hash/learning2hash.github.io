---
layout: publication
title: Deep Hashing with Hash-Consistent Large Margin Proxy Embeddings
authors: Morgado et al.
conference: International Journal of Computer Vision
year: 2020
bibkey: morgado2020deep
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/pdf/2007.13912.pdf'}]
tags: [Neural Hashing, Hashing Methods]
---
Image hash codes are produced by binarizing
the embeddings of convolutional neural networks (CNN)
trained for either classification or retrieval. While proxy
embeddings achieve good performance on both tasks,
they are non-trivial to binarize, due to a rotational ambiguity that encourages non-binary embeddings. The use
of a fixed set of proxies (weights of the CNN classification layer) is proposed to eliminate this ambiguity, and
a procedure to design proxy sets that are nearly optimal
for both classification and hashing is introduced. The
resulting hash-consistent large margin (HCLM) proxies
are shown to encourage saturation of hashing units, thus
guaranteeing a small binarization error, while producing
highly discriminative hash-codes. A semantic extension
(sHCLM), aimed to improve hashing performance in
a transfer scenario, is also proposed. Extensive experiments show that sHCLM embeddings achieve significant
improvements over state-of-the-art hashing procedures
on several small and large datasets, both within and
beyond the set of training classes.