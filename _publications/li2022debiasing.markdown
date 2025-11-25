---
layout: publication
title: Debiasing Neural Retrieval Via In-batch Balancing Regularization
authors: Yuantong Li, Xiaokai Wei, Zijian Wang, Shen Wang, Parminder Bhatia, Xiaofei
  Ma, Andrew Arnold
conference: Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing
  (GeBNLP)
year: 2022
bibkey: li2022debiasing
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.09240'}]
tags: ["Datasets", "Evaluation"]
short_authors: Li et al.
---
People frequently interact with information retrieval (IR) systems, however,
IR models exhibit biases and discrimination towards various demographics. The
in-processing fair ranking methods provide a trade-offs between accuracy and
fairness through adding a fairness-related regularization term in the loss
function. However, there haven't been intuitive objective functions that depend
on the click probability and user engagement to directly optimize towards this.
In this work, we propose the In-Batch Balancing Regularization (IBBR) to
mitigate the ranking disparity among subgroups. In particular, we develop a
differentiable \textit\{normed Pairwise Ranking Fairness\} (nPRF) and leverage
the T-statistics on top of nPRF over subgroups as a regularization to improve
fairness. Empirical results with the BERT-based neural rankers on the MS MARCO
Passage Retrieval dataset with the human-annotated non-gendered queries
benchmark \citep\{rekabsaz2020neural\} show that our IBBR method with nPRF
achieves significantly less bias with minimal degradation in ranking
performance compared with the baseline.