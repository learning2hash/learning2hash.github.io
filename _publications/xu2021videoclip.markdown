---
layout: publication
title: 'Videoclip: Contrastive Pre-training For Zero-shot Video-text Understanding'
authors: Hu Xu, Gargi Ghosh, Po-Yao Huang, Dmytro Okhonko, Armen Aghajanyan, Florian
  Metze, Luke Zettlemoyer, Christoph Feichtenhofer
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: xu2021videoclip
citations: 266
additional_links: [{name: Code, url: 'https://github.com/pytorch/fairseq/tree/main/examples/MMPT'},
  {name: Paper, url: 'https://arxiv.org/abs/2109.14084'}]
tags: ["EMNLP", "Few Shot & Zero Shot"]
short_authors: Xu et al.
---
We present VideoCLIP, a contrastive approach to pre-train a unified model for
zero-shot video and text understanding, without using any labels on downstream
tasks. VideoCLIP trains a transformer for video and text by contrasting
temporally overlapping positive video-text pairs with hard negatives from
nearest neighbor retrieval. Our experiments on a diverse series of downstream
tasks, including sequence-level text-video retrieval, VideoQA, token-level
action localization, and action segmentation reveal state-of-the-art
performance, surpassing prior work, and in some cases even outperforming
supervised approaches. Code is made available at
https://github.com/pytorch/fairseq/tree/main/examples/MMPT.