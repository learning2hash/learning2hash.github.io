---
layout: publication
title: Semantic-preserving Augmentation For Robust Image-text Retrieval
authors: Sunwoo Kim, Kyuhong Shim, Luong Trung Nguyen, Byonghyo Shim
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: kim2023semantic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.05692'}]
tags: [ICASSP, Datasets, Text Retrieval, Robustness, Evaluation]
short_authors: Kim et al.
---
Image text retrieval is a task to search for the proper textual descriptions
of the visual world and vice versa. One challenge of this task is the
vulnerability to input image and text corruptions. Such corruptions are often
unobserved during the training, and degrade the retrieval model decision
quality substantially. In this paper, we propose a novel image text retrieval
technique, referred to as robust visual semantic embedding (RVSE), which
consists of novel image-based and text-based augmentation techniques called
semantic preserving augmentation for image (SPAugI) and text (SPAugT). Since
SPAugI and SPAugT change the original data in a way that its semantic
information is preserved, we enforce the feature extractors to generate
semantic aware embedding vectors regardless of the corruption, improving the
model robustness significantly. From extensive experiments using benchmark
datasets, we show that RVSE outperforms conventional retrieval schemes in terms
of image-text retrieval performance.