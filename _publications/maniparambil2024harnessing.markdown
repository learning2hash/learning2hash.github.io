---
layout: publication
title: Harnessing Frozen Unimodal Encoders For Flexible Multimodal Alignment
authors: Mayug Maniparambil, Raiymbek Akshulakov, Yasser Abdelaziz Dahou Djilali,
  Sanath Narayan, Ankit Singh, Noel E. O'Connor
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: maniparambil2024harnessing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.19425'}]
tags: ["CVPR", "Datasets", "Few Shot & Zero Shot", "Text Retrieval", "Tools & Libraries"]
short_authors: Maniparambil et al.
---
Recent contrastive multimodal vision-language models like CLIP have
demonstrated robust open-world semantic understanding, becoming the standard
image backbones for vision-language applications. However, recent findings
suggest high semantic similarity between well-trained unimodal encoders, which
raises a key question: Is there a plausible way to connect unimodal backbones
for vision-language tasks? To this end, we propose a novel framework that
aligns vision and language using frozen unimodal encoders. It involves
selecting semantically similar encoders in the latent space, curating a
concept-rich dataset of image-caption pairs, and training simple MLP
projectors. We evaluated our approach on 12 zero-shot classification datasets
and 2 image-text retrieval datasets. Our best model, utilizing DINOv2 and
All-Roberta-Large text encoder, achieves 76\(%\) accuracy on ImageNet with a
20-fold reduction in data and 65-fold reduction in compute requirements
compared multi-modal alignment where models are trained from scratch. The
proposed framework enhances the accessibility of multimodal model development
while enabling flexible adaptation across diverse scenarios. Code and curated
datasets are available at \texttt\{github.com/mayug/freeze-align\}.