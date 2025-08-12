---
layout: publication
title: Universal Few-shot Learning Of Dense Prediction Tasks With Visual Token Matching
authors: Donggyun Kim, Jinwoo Kim, Seongwoong Cho, Chong Luo, Seunghoon Hong
conference: Arxiv
year: 2023
bibkey: kim2023universal
citations: 2
additional_links: [{name: Code, url: 'https://github.com/GitGyun/visual_token_matching'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.14969'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Kim et al.
---
Dense prediction tasks are a fundamental class of problems in computer
vision. As supervised methods suffer from high pixel-wise labeling cost, a
few-shot learning solution that can learn any dense task from a few labeled
images is desired. Yet, current few-shot learning methods target a restricted
set of tasks such as semantic segmentation, presumably due to challenges in
designing a general and unified model that is able to flexibly and efficiently
adapt to arbitrary tasks of unseen semantics. We propose Visual Token Matching
(VTM), a universal few-shot learner for arbitrary dense prediction tasks. It
employs non-parametric matching on patch-level embedded tokens of images and
labels that encapsulates all tasks. Also, VTM flexibly adapts to any task with
a tiny amount of task-specific parameters that modulate the matching algorithm.
We implement VTM as a powerful hierarchical encoder-decoder architecture
involving ViT backbones where token matching is performed at multiple feature
hierarchies. We experiment VTM on a challenging variant of Taskonomy dataset
and observe that it robustly few-shot learns various unseen dense prediction
tasks. Surprisingly, it is competitive with fully supervised baselines using
only 10 labeled examples of novel tasks (0.004% of full supervision) and
sometimes outperforms using 0.1% of full supervision. Codes are available at
https://github.com/GitGyun/visual_token_matching.