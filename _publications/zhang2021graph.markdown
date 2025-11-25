---
layout: publication
title: Graph Convolution For Re-ranking In Person Re-identification
authors: Yuqi Zhang, Qian Qi, Chong Liu, Weihua Chen, Fan Wang, Hao Li, Rong Jin
conference: Arxiv
year: 2021
bibkey: zhang2021graph
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.02220'}]
tags: ["Distance Metric Learning", "Graph Based ANN", "Image Retrieval", "Re-Ranking", "Video Retrieval"]
short_authors: Zhang et al.
---
Nowadays, deep learning is widely applied to extract features for similarity
computation in person re-identification (re-ID) and have achieved great
success. However, due to the non-overlapping between training and testing IDs,
the difference between the data used for model training and the testing data
makes the performance of learned feature degraded during testing. Hence,
re-ranking is proposed to mitigate this issue and various algorithms have been
developed. However, most of existing re-ranking methods focus on replacing the
Euclidean distance with sophisticated distance metrics, which are not friendly
to downstream tasks and hard to be used for fast retrieval of massive data in
real applications. In this work, we propose a graph-based re-ranking method to
improve learned features while still keeping Euclidean distance as the
similarity metric. Inspired by graph convolution networks, we develop an
operator to propagate features over an appropriate graph. Since graph is the
essential key for the propagation, two important criteria are considered for
designing the graph, and three different graphs are explored accordingly.
Furthermore, a simple yet effective method is proposed to generate a profile
vector for each tracklet in videos, which helps extend our method to video
re-ID. Extensive experiments on three benchmark data sets, e.g., Market-1501,
Duke, and MARS, demonstrate the effectiveness of our proposed approach.