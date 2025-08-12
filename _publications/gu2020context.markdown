---
layout: publication
title: Context-aware Feature Generation For Zero-shot Semantic Segmentation
authors: Zhangxuan Gu, Siyuan Zhou, Li Niu, Zihan Zhao, Liqing Zhang
conference: Proceedings of the 28th ACM International Conference on Multimedia
year: 2020
bibkey: gu2020context
citations: 95
additional_links: [{name: Code, url: 'https://github.com/bcmi/CaGNet-Zero-Shot-Semantic-Segmentation'},
  {name: Paper, url: 'https://arxiv.org/abs/2008.06893'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Gu et al.
---
Existing semantic segmentation models heavily rely on dense pixel-wise
annotations. To reduce the annotation pressure, we focus on a challenging task
named zero-shot semantic segmentation, which aims to segment unseen objects
with zero annotations. This task can be accomplished by transferring knowledge
across categories via semantic word embeddings. In this paper, we propose a
novel context-aware feature generation method for zero-shot segmentation named
CaGNet. In particular, with the observation that a pixel-wise feature highly
depends on its contextual information, we insert a contextual module in a
segmentation network to capture the pixel-wise contextual information, which
guides the process of generating more diverse and context-aware features from
semantic word embeddings. Our method achieves state-of-the-art results on three
benchmark datasets for zero-shot segmentation. Codes are available at:
https://github.com/bcmi/CaGNet-Zero-Shot-Semantic-Segmentation.