---
layout: publication
title: 'Pretrain Like Your Inference: Masked Tuning Improves Zero-shot Composed Image
  Retrieval'
authors: Junyang Chen, Hanjiang Lai
conference: Arxiv
year: 2023
bibkey: chen2023pretrain
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Chen-Junyang-cn/PLI'}, {
    name: Paper, url: 'https://arxiv.org/abs/2311.07622'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Image Retrieval", "Self-Supervised"]
short_authors: Junyang Chen, Hanjiang Lai
---
Zero-shot composed image retrieval (ZS-CIR), which takes a textual
modification and a reference image as a query to retrieve a target image
without triplet labeling, has gained more and more attention in data mining.
Current ZS-CIR research mainly relies on the generalization ability of
pre-trained vision-language models, e.g., CLIP. However, the pre-trained
vision-language models and CIR tasks have substantial discrepancies, where the
vision-language models focus on learning the similarities but CIR aims to learn
the modifications of the image guided by text. In this paper, we introduce a
novel unlabeled and pre-trained masked tuning approach, which reduces the gap
between the pre-trained vision-language model and the downstream CIR task.
First, to reduce the gap, we reformulate the contrastive learning of the
vision-language model as the CIR task, where we randomly mask input image
patches to generate \(\langle\)masked image, text, image\(\rangle\) triplet from an
image-text pair. Then, we propose a simple but novel pre-trained masked tuning
method, which uses the text and the masked image to learn the modifications of
the original image. With such a simple design, the proposed masked tuning can
learn to better capture fine-grained text-guided modifications. Extensive
experimental results demonstrate the significant superiority of our approach
over the baseline models on four ZS-CIR datasets, including FashionIQ, CIRR,
CIRCO, and GeneCIS. Our codes are available at
https://github.com/Chen-Junyang-cn/PLI