---
layout: publication
title: 'Anomaly Clustering: Grouping Images Into Coherent Clusters Of Anomaly Types'
authors: Kihyuk Sohn, Jinsung Yoon, Chun-liang Li, Chen-yu Lee, Tomas Pfister
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: sohn2021anomaly
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.11573'}]
tags: ["Unsupervised"]
short_authors: Sohn et al.
---
We study anomaly clustering, grouping data into coherent clusters of anomaly
types. This is different from anomaly detection that aims to divide anomalies
from normal data. Unlike object-centered image clustering, anomaly clustering
is particularly challenging as anomalous patterns are subtle and local. We
present a simple yet effective clustering framework using a patch-based
pretrained deep embeddings and off-the-shelf clustering methods. We define a
distance function between images, each of which is represented as a bag of
embeddings, by the Euclidean distance between weighted averaged embeddings. The
weight defines the importance of instances (i.e., patch embeddings) in the bag,
which may highlight defective regions. We compute weights in an unsupervised
way or in a semi-supervised way when labeled normal data is available.
Extensive experimental studies show the effectiveness of the proposed
clustering framework along with a novel distance function upon exist-ing
multiple instance or deep clustering frameworks. Over-all, our framework
achieves 0.451 and 0.674 normalized mutual information scores on MVTec object
and texture categories and further improve with a few labeled normal data
(0.577, 0.669), far exceeding the baselines (0.244, 0.273) or state-of-the-art
deep clustering methods (0.176, 0.277).