---
layout: publication
title: 'Bloomcoreset: Fast Coreset Sampling Using Bloom Filters For Fine-grained Self-supervised
  Learning'
authors: Prajwal Singh, Gautam Vashishtha, Indra Deep Mastan, Shanmuganathan Raman
conference: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2025
bibkey: singh2024bloomcoreset
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.16942'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "ICASSP", "Self-Supervised"]
short_authors: Singh et al.
---
The success of deep learning in supervised fine-grained recognition for
domain-specific tasks relies heavily on expert annotations. The Open-Set for
fine-grained Self-Supervised Learning (SSL) problem aims to enhance performance
on downstream tasks by strategically sampling a subset of images (the Core-Set)
from a large pool of unlabeled data (the Open-Set). In this paper, we propose a
novel method, BloomCoreset, that significantly reduces sampling time from
Open-Set while preserving the quality of samples in the coreset. To achieve
this, we utilize Bloom filters as an innovative hashing mechanism to store both
low- and high-level features of the fine-grained dataset, as captured by
Open-CLIP, in a space-efficient manner that enables rapid retrieval of the
coreset from the Open-Set. To show the effectiveness of the sampled coreset, we
integrate the proposed method into the state-of-the-art fine-grained SSL
framework, SimCore [1]. The proposed algorithm drastically outperforms the
sampling strategy of the baseline in SimCore [1] with a \\(98.5%\\) reduction in
sampling time with a mere \\(0.83%\\) average trade-off in accuracy calculated
across \\(11\\) downstream datasets.