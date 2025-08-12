---
layout: publication
title: Artistic-style Text Detector And A New Movie-poster Dataset
authors: Aoxiang Ning, Yiting Wei, Minglong Xue, Senming Zhong
conference: Arxiv
year: 2024
bibkey: ning2024artistic
citations: 0
additional_links: [{name: Code, url: 'https://github.com/biedaxiaohua/Artistic-style-text-detection'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.16307'}]
tags: ["Datasets"]
short_authors: Ning et al.
---
Although current text detection algorithms demonstrate effectiveness in
general scenarios, their performance declines when confronted with
artistic-style text featuring complex structures. This paper proposes a method
that utilizes Criss-Cross Attention and residual dense block to address the
incomplete and misdiagnosis of artistic-style text detection by current
algorithms. Specifically, our method mainly consists of a feature extraction
backbone, a feature enhancement network, a multi-scale feature fusion module,
and a boundary discrimination module. The feature enhancement network
significantly enhances the model's perceptual capabilities in complex
environments by fusing horizontal and vertical contextual information, allowing
it to capture detailed features overlooked in artistic-style text. We
incorporate residual dense block into the Feature Pyramid Network to suppress
the effect of background noise during feature fusion. Aiming to omit the
complex post-processing, we explore a boundary discrimination module that
guides the correct generation of boundary proposals. Furthermore, given that
movie poster titles often use stylized art fonts, we collected a Movie-Poster
dataset to address the scarcity of artistic-style text data. Extensive
experiments demonstrate that our proposed method performs superiorly on the
Movie-Poster dataset and produces excellent results on multiple benchmark
datasets. The code and the Movie-Poster dataset will be available at:
https://github.com/biedaxiaohua/Artistic-style-text-detection