---
layout: publication
title: '\(k\)nn-ner: Named Entity Recognition With Nearest Neighbor Search'
authors: Shuhe Wang, Xiaoya Li, Yuxian Meng, Tianwei Zhang, Rongbin Ouyang, Jiwei
  Li, Guoyin Wang
conference: Arxiv
year: 2022
bibkey: wang2022k
citations: 10
additional_links: [{name: Code, url: 'https://github.com/ShannonAI/KNN-NER.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.17103'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Wang et al.
---
Inspired by recent advances in retrieval augmented methods in
NLP~\citep\{khandelwal2019generalization,khandelwal2020nearest,meng2021gnn\}, in
this paper, we introduce a \(k\) nearest neighbor NER (\(k\)NN-NER) framework,
which augments the distribution of entity labels by assigning \(k\) nearest
neighbors retrieved from the training set. This strategy makes the model more
capable of handling long-tail cases, along with better few-shot learning
abilities. \(k\)NN-NER requires no additional operation during the training
phase, and by interpolating \(k\) nearest neighbors search into the vanilla NER
model, \(k\)NN-NER consistently outperforms its vanilla counterparts: we achieve
a new state-of-the-art F1-score of 72.03 (+1.25) on the Chinese Weibo dataset
and improved results on a variety of widely used NER benchmarks. Additionally,
we show that \(k\)NN-NER can achieve comparable results to the vanilla NER model
with 40% less amount of training data. Code available at
https://github.com/ShannonAI/KNN-NER.