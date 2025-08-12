---
layout: publication
title: Incremental False Negative Detection For Contrastive Learning
authors: Tsai-Shien Chen, Wei-Chih Hung, Hung-Yu Tseng, Shao-Yi Chien, Ming-Hsuan
  Yang
conference: Arxiv
year: 2021
bibkey: chen2021incremental
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.03719'}]
tags: ["Self-Supervised"]
short_authors: Chen et al.
---
Self-supervised learning has recently shown great potential in vision tasks
through contrastive learning, which aims to discriminate each image, or
instance, in the dataset. However, such instance-level learning ignores the
semantic relationship among instances and sometimes undesirably repels the
anchor from the semantically similar samples, termed as "false negatives". In
this work, we show that the unfavorable effect from false negatives is more
significant for the large-scale datasets with more semantic concepts. To
address the issue, we propose a novel self-supervised contrastive learning
framework that incrementally detects and explicitly removes the false negative
samples. Specifically, following the training process, our method dynamically
detects increasing high-quality false negatives considering that the encoder
gradually improves and the embedding space becomes more semantically
structural. Next, we discuss two strategies to explicitly remove the detected
false negatives during contrastive learning. Extensive experiments show that
our framework outperforms other self-supervised contrastive learning methods on
multiple benchmarks in a limited resource setup.