---
layout: publication
title: 'RWKV-CLIP: A Robust Vision-language Representation Learner'
authors: Tiancheng Gu, Kaicheng Yang, Xiang An, Ziyong Feng, Dongnan Liu, Weidong
  Cai, Jiankang Deng
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: gu2024rwkv
citations: 8
additional_links: [{name: Code, url: 'https://github.com/deepglint/RWKV-CLIP'}, {
    name: Paper, url: 'https://arxiv.org/abs/2406.06973'}]
tags: [Evaluation, Few-shot & Zero-shot, Datasets, Scalability, Tools & Libraries,
  Text Retrieval, EMNLP]
short_authors: Gu et al.
---
Contrastive Language-Image Pre-training (CLIP) has significantly improved
performance in various vision-language tasks by expanding the dataset with
image-text pairs obtained from websites. This paper further explores CLIP from
the perspectives of data and model architecture. To address the prevalence of
noisy data and enhance the quality of large-scale image-text data crawled from
the internet, we introduce a diverse description generation framework that can
leverage Large Language Models (LLMs) to synthesize and refine content from
web-based texts, synthetic captions, and detection tags. Furthermore, we
propose RWKV-CLIP, the first RWKV-driven vision-language representation
learning model that combines the effective parallel training of transformers
with the efficient inference of RNNs. Comprehensive experiments across various
model scales and pre-training datasets demonstrate that RWKV-CLIP is a robust
and efficient vision-language representation learner, it achieves
state-of-the-art performance in several downstream tasks, including linear
probe, zero-shot classification, and zero-shot image-text retrieval. To
facilitate future research, the code and pre-trained models are released at
https://github.com/deepglint/RWKV-CLIP