---
layout: publication
title: Vision-language Dataset Distillation
authors: Xindi Wu, Byron Zhang, Zhiwei Deng, Olga Russakovsky
conference: Arxiv
year: 2023
bibkey: wu2023vision
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.07545'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Wu et al.
---
Dataset distillation methods reduce large-scale datasets to smaller sets of
synthetic data, preserving sufficient information to quickly train a new model
from scratch. However, prior work on dataset distillation has focused
exclusively on image classification datasets, whereas modern large-scale
datasets are primarily vision-language datasets. In this work, we design the
first vision-language dataset distillation method, building on the idea of
trajectory matching. A key challenge is that vision-language datasets do not
have a set of discrete classes. To overcome this, our proposed method jointly
distills image-text pairs in a contrastive formulation. Further, we leverage
Low-Rank Adaptation (LoRA) matching to enable more efficient and effective
trajectory matching in complex modern vision-language models. Since there are
no existing baselines, we compare our distillation approach with three adapted
vision-language coreset selection methods. We demonstrate significant
improvements on the challenging Flickr30K and COCO retrieval benchmarks: for
example, on Flickr30K, the best coreset selection method selecting 1000
image-text pairs for training achieves only 5.6% image-to-text retrieval
accuracy (i.e., recall@1); in contrast, our dataset distillation almost doubles
that to 9.9% with just 100 training pairs, an order of magnitude fewer.