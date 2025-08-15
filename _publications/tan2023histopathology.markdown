---
layout: publication
title: Histopathology Image Classification Using Deep Manifold Contrastive Learning
authors: Jing Wei Tan, Won-Ki Jeong
conference: Lecture Notes in Computer Science
year: 2023
bibkey: tan2023histopathology
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14459'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Robustness"]
short_authors: Jing Wei Tan, Won-Ki Jeong
---
Contrastive learning has gained popularity due to its robustness with good
feature representation performance. However, cosine distance, the commonly used
similarity metric in contrastive learning, is not well suited to represent the
distance between two data points, especially on a nonlinear feature manifold.
Inspired by manifold learning, we propose a novel extension of contrastive
learning that leverages geodesic distance between features as a similarity
metric for histopathology whole slide image classification. To reduce the
computational overhead in manifold learning, we propose geodesic-distance-based
feature clustering for efficient contrastive loss evaluation using prototypes
without time-consuming pairwise feature similarity comparison. The efficacy of
the proposed method is evaluated on two real-world histopathology image
datasets. Results demonstrate that our method outperforms state-of-the-art
cosine-distance-based contrastive learning methods.