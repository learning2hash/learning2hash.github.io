---
layout: publication
title: 'NEVLP: Noise-robust Framework For Efficient Vision-language Pre-training'
authors: Yiyi Tao, Zhuoyue Wang, Hang Zhang, Lun Wang
conference: Arxiv
year: 2024
bibkey: tao2024nevlp
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.09582'}]
tags: [Evaluation, Self-Supervised, Datasets, Scalability, Tools & Libraries, Text
    Retrieval]
short_authors: Tao et al.
---
The success of Vision Language Models (VLMs) on various vision-language tasks
heavily relies on pre-training with large scale web-crawled datasets. However,
the noisy and incomplete nature of web data makes dataset scale crucial for
performance, rendering end-to-end training increasingly prohibitive. In this
paper, we propose NEVLP, a noise-robust framework for efficient vision-language
pre-training that requires less pre-training data. Specifically, we bridge the
modality gap between a frozen image encoder and a large language model with a
transformer and introduce two innovative learning strategies: noise-adaptive
learning and concept-enhanced learning to mitigate the impact of noise. In
noise-adaptive learning, we estimate the noise probability of each image-text
pair based on the transformer's memorization effect and employ noise-adaptive
regularization on image-text contrastive learning to condition cross-modal
alignment. In concept-enhanced learning, we enrich incomplete text by
incorporating visual concepts (objects in the image) to provide prior
information about existing objects for image-text matching and image-grounded
text generation, thereby mitigating text incompletion. Our framework
effectively utilizes noisy web data and achieves state-of-the-art performance
with less pre-training data across a wide range of vision-language tasks,
including image-text retrieval, image captioning, and visual question
answering.