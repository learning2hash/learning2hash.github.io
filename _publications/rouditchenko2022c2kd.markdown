---
layout: publication
title: 'C2KD: Cross-lingual Cross-modal Knowledge Distillation For Multilingual Text-video
  Retrieval'
authors: Andrew Rouditchenko, Yung-Sung Chuang, Nina Shvetsova, Samuel Thomas, Rogerio
  Feris, Brian Kingsbury, Leonid Karlinsky, David Harwath, Hilde Kuehne, James Glass
conference: Arxiv
year: 2022
bibkey: rouditchenko2022c2kd
citations: 0
additional_links: [{name: Code, url: 'https://github.com/roudimit/c2kd'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.03625'}]
tags: [Video Retrieval, Evaluation, Datasets]
short_authors: Rouditchenko et al.
---
Multilingual text-video retrieval methods have improved significantly in
recent years, but the performance for other languages lags behind English. We
propose a Cross-Lingual Cross-Modal Knowledge Distillation method to improve
multilingual text-video retrieval. Inspired by the fact that English text-video
retrieval outperforms other languages, we train a student model using input
text in different languages to match the cross-modal predictions from teacher
models using input text in English. We propose a cross entropy based objective
which forces the distribution over the student's text-video similarity scores
to be similar to those of the teacher models. We introduce a new multilingual
video dataset, Multi-YouCook2, by translating the English captions in the
YouCook2 video dataset to 8 other languages. Our method improves multilingual
text-video retrieval performance on Multi-YouCook2 and several other datasets
such as Multi-MSRVTT and VATEX. We also conducted an analysis on the
effectiveness of different multilingual text models as teachers. The code,
models, and dataset are available at https://github.com/roudimit/c2kd.