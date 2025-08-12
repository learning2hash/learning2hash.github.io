---
layout: publication
title: A Study On Representation Transfer For Few-shot Learning
authors: Chun-Nam Yu, Yi Xie
conference: Arxiv
year: 2022
bibkey: yu2022study
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02073'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chun-Nam Yu, Yi Xie
---
Few-shot classification aims to learn to classify new object categories well
using only a few labeled examples. Transferring feature representations from
other models is a popular approach for solving few-shot classification
problems. In this work we perform a systematic study of various feature
representations for few-shot classification, including representations learned
from MAML, supervised classification, and several common self-supervised tasks.
We find that learning from more complex tasks tend to give better
representations for few-shot classification, and thus we propose the use of
representations learned from multiple tasks for few-shot classification.
Coupled with new tricks on feature selection and voting to handle the issue of
small sample size, our direct transfer learning method offers performance
comparable to state-of-art on several benchmark datasets.