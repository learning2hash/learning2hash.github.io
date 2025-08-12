---
layout: publication
title: 'Less Is More: A Closer Look At Semantic-based Few-shot Learning'
authors: Chunpeng Zhou, Haishuai Wang, Xilu Yuan, Zhi Yu, Jiajun Bu
conference: Information Fusion
year: 2024
bibkey: zhou2024less
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.05010'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhou et al.
---
Few-shot Learning aims to learn and distinguish new categories with a very
limited number of available images, presenting a significant challenge in the
realm of deep learning. Recent researchers have sought to leverage the
additional textual or linguistic information of these rare categories with a
pre-trained language model to facilitate learning, thus partially alleviating
the problem of insufficient supervision signals. However, the full potential of
the textual information and pre-trained language model have been underestimated
in the few-shot learning till now, resulting in limited performance
enhancements. To address this, we propose a simple but effective framework for
few-shot learning tasks, specifically designed to exploit the textual
information and language model. In more detail, we explicitly exploit the
zero-shot capability of the pre-trained language model with the learnable
prompt. And we just add the visual feature with the textual feature for
inference directly without the intricate designed fusion modules in previous
works. Additionally, we apply the self-ensemble and distillation to further
enhance these components. Our extensive experiments conducted across four
widely used few-shot datasets demonstrate that our simple framework achieves
impressive results. Particularly noteworthy is its outstanding performance in
the 1-shot learning task, surpassing state-of-the-art methods by an average of
3.0% in classification accuracy. \footnote\{We will make the source codes of
the proposed framework publicly available upon acceptance. \}.