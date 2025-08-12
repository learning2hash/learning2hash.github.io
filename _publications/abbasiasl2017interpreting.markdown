---
layout: publication
title: Interpreting Convolutional Neural Networks Through Compression
authors: Reza Abbasi-Asl, Bin Yu
conference: Arxiv
year: 2017
bibkey: abbasiasl2017interpreting
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.02329'}]
tags: ["Evaluation"]
short_authors: Reza Abbasi-Asl, Bin Yu
---
Convolutional neural networks (CNNs) achieve state-of-the-art performance in
a wide variety of tasks in computer vision. However, interpreting CNNs still
remains a challenge. This is mainly due to the large number of parameters in
these networks. Here, we investigate the role of compression and particularly
pruning filters in the interpretation of CNNs. We exploit our recently-proposed
greedy structural compression scheme that prunes filters in a trained CNN. In
our compression, the filter importance index is defined as the classification
accuracy reduction (CAR) of the network after pruning that filter. The filters
are then iteratively pruned based on the CAR index. We demonstrate the
interpretability of CAR-compressed CNNs by showing that our algorithm prunes
filters with visually redundant pattern selectivity. Specifically, we show the
importance of shape-selective filters for object recognition, as opposed to
color-selective filters. Out of top 20 CAR-pruned filters in AlexNet, 17 of
them in the first layer and 14 of them in the second layer are color-selective
filters. Finally, we introduce a variant of our CAR importance index that
quantifies the importance of each image class to each CNN filter. We show that
the most and the least important class labels present a meaningful
interpretation of each filter that is consistent with the visualized pattern
selectivity of that filter.