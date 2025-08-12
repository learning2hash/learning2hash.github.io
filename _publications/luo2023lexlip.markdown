---
layout: publication
title: 'Lexlip: Lexicon-bottlenecked Language-image Pre-training For Large-scale Image-text
  Retrieval'
authors: Ziyang Luo, Pu Zhao, Can Xu, Xiubo Geng, Tao Shen, Chongyang Tao, Jing Ma,
  Qingwen Lin, Daxin Jiang
conference: Arxiv
year: 2023
bibkey: luo2023lexlip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.02908'}]
tags: ["Scalability", "Text Retrieval", "Tools & Libraries"]
short_authors: Luo et al.
---
Image-text retrieval (ITR) is a task to retrieve the relevant images/texts,
given the query from another modality. The conventional dense retrieval
paradigm relies on encoding images and texts into dense representations using
dual-stream encoders, however, it faces challenges with low retrieval speed in
large-scale retrieval scenarios. In this work, we propose the lexicon-weighting
paradigm, where sparse representations in vocabulary space are learned for
images and texts to take advantage of the bag-of-words models and efficient
inverted indexes, resulting in significantly reduced retrieval latency. A
crucial gap arises from the continuous nature of image data, and the
requirement for a sparse vocabulary space representation. To bridge this gap,
we introduce a novel pre-training framework, Lexicon-Bottlenecked
Language-Image Pre-Training (LexLIP), that learns importance-aware lexicon
representations. This framework features lexicon-bottlenecked modules between
the dual-stream encoders and weakened text decoders, allowing for constructing
continuous bag-of-words bottlenecks to learn lexicon-importance distributions.
Upon pre-training with same-scale data, our LexLIP achieves state-of-the-art
performance on two benchmark ITR datasets, MSCOCO and Flickr30k. Furthermore,
in large-scale retrieval scenarios, LexLIP outperforms CLIP with a 5.5 ~ 221.3X
faster retrieval speed and 13.2 ~ 48.8X less index storage memory.