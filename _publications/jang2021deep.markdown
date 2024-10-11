---
layout: publication
title: Deep Hash Distillation For Image Retrieval
authors: Jang Young Kyun, Gu Geonmo, Ko Byungsoo, Kang Isaac, Cho Nam Ik
conference: "Arxiv"
year: 2021
bibkey: jang2021deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.08816"}
tags: ['ARXIV', 'Image Retrieval', 'Independent', 'Quantisation']
---
In hash-based image retrieval systems, degraded or transformed inputs usually generate different codes from the original, deteriorating the retrieval accuracy. To mitigate this issue, data augmentation can be applied during training. However, even if augmented samples of an image are similar in real feature space, the quantization can scatter them far away in Hamming space. This results in representation discrepancies that can impede training and degrade performance. In this work, we propose a novel self-distilled hashing scheme to minimize the discrepancy while exploiting the potential of augmented data. By transferring the hash knowledge of the weakly-transformed samples to the strong ones, we make the hash code insensitive to various transformations. We also introduce hash proxy-based similarity learning and binary cross entropy-based quantization loss to provide fine quality hash codes. Ultimately, we construct a deep hashing framework that not only improves the existing deep hashing approaches, but also achieves the state-of-the-art retrieval results. Extensive experiments are conducted and confirm the effectiveness of our work.
