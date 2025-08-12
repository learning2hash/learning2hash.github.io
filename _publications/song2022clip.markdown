---
layout: publication
title: 'CLIP Models Are Few-shot Learners: Empirical Studies On VQA And Visual Entailment'
authors: Haoyu Song, Li Dong, Wei-Nan Zhang, Ting Liu, Furu Wei
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: song2022clip
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.07190'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Song et al.
---
CLIP has shown a remarkable zero-shot capability on a wide range of vision
tasks. Previously, CLIP is only regarded as a powerful visual encoder. However,
after being pre-trained by language supervision from a large amount of
image-caption pairs, CLIP itself should also have acquired some few-shot
abilities for vision-language tasks. In this work, we empirically show that
CLIP can be a strong vision-language few-shot learner by leveraging the power
of language. We first evaluate CLIP's zero-shot performance on a typical visual
question answering task and demonstrate a zero-shot cross-modality transfer
capability of CLIP on the visual entailment task. Then we propose a
parameter-efficient fine-tuning strategy to boost the few-shot performance on
the vqa task. We achieve competitive zero/few-shot results on the visual
question answering and visual entailment tasks without introducing any
additional pre-training procedure.