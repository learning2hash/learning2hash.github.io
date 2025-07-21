---
layout: publication
title: A Strong and Robust Baseline for Text-Image Matching
authors: Liu Fangyu, Ye Rongtian
conference: 'Proceedings of the 57th Annual Meeting of the Association for Computational
  Linguistics: Student Research Workshop'
year: 2019
bibkey: liu2019strong
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.01205'}]
tags: []
---
We review the current schemes of text-image matching models and propose
improvements for both training and inference. First, we empirically show
limitations of two popular loss (sum and max-margin loss) widely used in
training text-image embeddings and propose a trade-off: a kNN-margin loss which
1) utilizes information from hard negatives and 2) is robust to noise as all
\\(K\\)-most hardest samples are taken into account, tolerating *pseudo*
negatives and outliers. Second, we advocate the use of Inverted Softmax
(\textsc\{Is\}) and Cross-modal Local Scaling (\textsc\{Csls\}) during inference to
mitigate the so-called hubness problem in high-dimensional embedding space,
enhancing scores of all metrics by a large margin.