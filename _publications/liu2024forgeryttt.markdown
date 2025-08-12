---
layout: publication
title: 'Forgeryttt: Zero-shot Image Manipulation Localization With Test-time Training'
authors: Weihuang Liu, Xi Shen, Chi-Man Pun, Xiaodong Cun
conference: Arxiv
year: 2024
bibkey: liu2024forgeryttt
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.04032'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Social media is increasingly plagued by realistic fake images, making it hard
to trust content. Previous algorithms to detect these fakes often fail in new,
real-world scenarios because they are trained on specific datasets. To address
the problem, we introduce ForgeryTTT, the first method leveraging test-time
training (TTT) to identify manipulated regions in images. The proposed approach
fine-tunes the model for each individual test sample, improving its
performance. ForgeryTTT first employs vision transformers as a shared image
encoder to learn both classification and localization tasks simultaneously
during the training-time training using a large synthetic dataset. Precisely,
the localization head predicts a mask to highlight manipulated areas. Given
such a mask, the input tokens can be divided into manipulated and genuine
groups, which are then fed into the classification head to distinguish between
manipulated and genuine parts. During test-time training, the predicted mask
from the localization head is used for the classification head to update the
image encoder for better adaptation. Additionally, using the classical dropout
strategy in each token group significantly improves performance and efficiency.
We test ForgeryTTT on five standard benchmarks. Despite its simplicity,
ForgeryTTT achieves a 20.1% improvement in localization accuracy compared to
other zero-shot methods and a 4.3% improvement over non-zero-shot techniques.
Our code and data will be released upon publication.