---
layout: publication
title: Semantic Granularity Metric Learning for Visual Search
authors: Manandhar Dipu, Bastan Muhammet, Yap Kim-hui
conference: Journal of Visual Communication and Image Representation
year: 2020
bibkey: manandhar2020semantic
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.06047'}]
tags: ["Image-Retrieval", "Distance-Metric-Learning"]
---
Deep metric learning applied to various applications has shown promising
results in identification, retrieval and recognition. Existing methods often do
not consider different granularity in visual similarity. However, in many
domain applications, images exhibit similarity at multiple granularities with
visual semantic concepts, e.g. fashion demonstrates similarity ranging from
clothing of the exact same instance to similar looks/design or a common
category. Therefore, training image triplets/pairs used for metric learning
inherently possess different degree of information. However, the existing
methods often treats them with equal importance during training. This hinders
capturing the underlying granularities in feature similarity required for
effective visual search.
  In view of this, we propose a new deep semantic granularity metric learning
(SGML) that develops a novel idea of leveraging attribute semantic space to
capture different granularity of similarity, and then integrate this
information into deep metric learning. The proposed method simultaneously
learns image attributes and embeddings using multitask CNNs. The two tasks are
not only jointly optimized but are further linked by the semantic granularity
similarity mappings to leverage the correlations between the tasks. To this
end, we propose a new soft-binomial deviance loss that effectively integrates
the degree of information in training samples, which helps to capture visual
similarity at multiple granularities. Compared to recent ensemble-based
methods, our framework is conceptually elegant, computationally simple and
provides better performance. We perform extensive experiments on benchmark
metric learning datasets and demonstrate that our method outperforms recent
state-of-the-art methods, e.g., 1-4.5% improvement in Recall@1 over the
previous state-of-the-arts [1],[2] on DeepFashion In-Shop dataset.