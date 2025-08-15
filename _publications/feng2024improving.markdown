---
layout: publication
title: Improving Composed Image Retrieval Via Contrastive Learning With Scaling Positives
  And Negatives
authors: Zhangchi Feng, Richong Zhang, Zhijie Nie
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: feng2024improving
citations: 2
additional_links: [{name: Code, url: 'https://github.com/BUAADreamer/SPN4CIR.'}, {
    name: Paper, url: 'https://arxiv.org/abs/2404.11317'}]
tags: ["Datasets", "Image Retrieval", "Self-Supervised", "Tools & Libraries"]
short_authors: Zhangchi Feng, Richong Zhang, Zhijie Nie
---
The Composed Image Retrieval (CIR) task aims to retrieve target images using
a composed query consisting of a reference image and a modified text. Advanced
methods often utilize contrastive learning as the optimization objective, which
benefits from adequate positive and negative examples. However, the triplet for
CIR incurs high manual annotation costs, resulting in limited positive
examples. Furthermore, existing methods commonly use in-batch negative
sampling, which reduces the negative number available for the model. To address
the problem of lack of positives, we propose a data generation method by
leveraging a multi-modal large language model to construct triplets for CIR. To
introduce more negatives during fine-tuning, we design a two-stage fine-tuning
framework for CIR, whose second stage introduces plenty of static
representations of negatives to optimize the representation space rapidly. The
above two improvements can be effectively stacked and designed to be
plug-and-play, easily applied to existing CIR models without changing their
original architectures. Extensive experiments and ablation analysis demonstrate
that our method effectively scales positives and negatives and achieves
state-of-the-art results on both FashionIQ and CIRR datasets. In addition, our
method also performs well in zero-shot composed image retrieval, providing a
new CIR solution for the low-resources scenario. Our code and data are released
at https://github.com/BUAADreamer/SPN4CIR.