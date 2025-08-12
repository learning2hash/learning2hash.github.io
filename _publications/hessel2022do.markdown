---
layout: publication
title: Do Androids Laugh At Electric Sheep? Humor "understanding" Benchmarks From
  The New Yorker Caption Contest
authors: "Jack Hessel, Ana Marasovi\u0107, Jena D. Hwang, Lillian Lee, Jeff da, Rowan\
  \ Zellers, Robert Mankoff, Yejin Choi"
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: hessel2022do
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.06293'}]
tags: ["Evaluation"]
short_authors: Hessel et al.
---
Large neural networks can now generate jokes, but do they really "understand"
humor? We challenge AI models with three tasks derived from the New Yorker
Cartoon Caption Contest: matching a joke to a cartoon, identifying a winning
caption, and explaining why a winning caption is funny. These tasks encapsulate
progressively more sophisticated aspects of "understanding" a cartoon; key
elements are the complex, often surprising relationships between images and
captions and the frequent inclusion of indirect and playful allusions to human
experience and culture. We investigate both multimodal and language-only
models: the former are challenged with the cartoon images directly, while the
latter are given multifaceted descriptions of the visual scene to simulate
human-level visual understanding. We find that both types of models struggle at
all three tasks. For example, our best multimodal models fall 30 accuracy
points behind human performance on the matching task, and, even when provided
ground-truth visual scene descriptors, human-authored explanations are
preferred head-to-head over the best machine-authored ones (few-shot GPT-4) in
more than 2/3 of cases. We release models, code, leaderboard, and corpus, which
includes newly-gathered annotations describing the image's locations/entities,
what's unusual in the scene, and an explanation of the joke.