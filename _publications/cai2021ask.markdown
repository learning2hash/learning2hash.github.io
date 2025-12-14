---
layout: publication
title: 'Ask&confirm: Active Detail Enriching For Cross-modal Retrieval With Partial
  Query'
authors: Guanyu Cai, Jun Zhang, Xinyang Jiang, Yifei Gong, Lianghua He, Fufu Yu, Pai
  Peng, Xiaowei Guo, Feiyue Huang, Xing Sun
conference: Arxiv
year: 2021
bibkey: cai2021ask
citations: 1
additional_links: [{name: Code, url: 'https://github.com/CuthbertCai/Ask-Confirm'},
  {name: Paper, url: 'https://arxiv.org/abs/2103.01654'}]
tags: [Evaluation, Supervised, Image Retrieval, Datasets, Multimodal Retrieval, Tools
    & Libraries]
short_authors: Cai et al.
---
Text-based image retrieval has seen considerable progress in recent years.
However, the performance of existing methods suffers in real life since the
user is likely to provide an incomplete description of an image, which often
leads to results filled with false positives that fit the incomplete
description. In this work, we introduce the partial-query problem and
extensively analyze its influence on text-based image retrieval. Previous
interactive methods tackle the problem by passively receiving users' feedback
to supplement the incomplete query iteratively, which is time-consuming and
requires heavy user effort. Instead, we propose a novel retrieval framework
that conducts the interactive process in an Ask-and-Confirm fashion, where AI
actively searches for discriminative details missing in the current query, and
users only need to confirm AI's proposal. Specifically, we propose an
object-based interaction to make the interactive retrieval more user-friendly
and present a reinforcement-learning-based policy to search for discriminative
objects. Furthermore, since fully-supervised training is often infeasible due
to the difficulty of obtaining human-machine dialog data, we present a
weakly-supervised training strategy that needs no human-annotated dialogs other
than a text-image dataset. Experiments show that our framework significantly
improves the performance of text-based image retrieval. Code is avaiable at
https://github.com/CuthbertCai/Ask-Confirm.