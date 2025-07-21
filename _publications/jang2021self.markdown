---
layout: publication
title: Self-supervised Product Quantization for Deep Unsupervised Image Retrieval
authors: Jang Young Kyun, Cho Nam Ik
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: jang2021self
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.02244'}]
tags: ["Unsupervised", "Supervised", "Quantization", "Self-Supervised", "ICCV"]
---
Supervised deep learning-based hash and vector quantization are enabling fast
and large-scale image retrieval systems. By fully exploiting label annotations,
they are achieving outstanding retrieval performances compared to the
conventional methods. However, it is painstaking to assign labels precisely for
a vast amount of training data, and also, the annotation process is
error-prone. To tackle these issues, we propose the first deep unsupervised
image retrieval method dubbed Self-supervised Product Quantization (SPQ)
network, which is label-free and trained in a self-supervised manner. We design
a Cross Quantized Contrastive learning strategy that jointly learns codewords
and deep visual descriptors by comparing individually transformed images
(views). Our method analyzes the image contents to extract descriptive
features, allowing us to understand image representations for accurate
retrieval. By conducting extensive experiments on benchmarks, we demonstrate
that the proposed method yields state-of-the-art results even without
supervised pretraining.