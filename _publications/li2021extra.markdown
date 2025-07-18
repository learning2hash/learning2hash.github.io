---
layout: publication
title: 'EXTRA: Explanation Ranking Datasets For Explainable Recommendation'
authors: Li Lei, Zhang Yongfeng, Chen Li
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: li2021extra
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.10315'}]
tags: [Survey Paper, Locality Sensitive Hashing, DATASETS, Hashing Methods, Alt, Recommender
    Systems, SIGIR, Evaluation]
---
Recently, research on explainable recommender systems has drawn much
attention from both academia and industry, resulting in a variety of
explainable models. As a consequence, their evaluation approaches vary from
model to model, which makes it quite difficult to compare the explainability of
different models. To achieve a standard way of evaluating recommendation
explanations, we provide three benchmark datasets for EXplanaTion RAnking
(denoted as EXTRA), on which explainability can be measured by ranking-oriented
metrics. Constructing such datasets, however, poses great challenges. First,
user-item-explanation triplet interactions are rare in existing recommender
systems, so how to find alternatives becomes a challenge. Our solution is to
identify nearly identical sentences from user reviews. This idea then leads to
the second challenge, i.e., how to efficiently categorize the sentences in a
dataset into different groups, since it has quadratic runtime complexity to
estimate the similarity between any two sentences. To mitigate this issue, we
provide a more efficient method based on Locality Sensitive Hashing (LSH) that
can detect near-duplicates in sub-linear time for a given query. Moreover, we
make our code publicly available to allow researchers in the community to
create their own datasets.