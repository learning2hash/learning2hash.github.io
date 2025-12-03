---
layout: publication
title: Learning Deep Representations By Mutual Information For Person Re-identification
authors: Peng Chen, Tong Jia, Pengfei Wu, Jianjun Wu, Dongyue Chen
conference: Arxiv
year: 2019
bibkey: chen2019learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05860'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Supervised", "Unsupervised"]
short_authors: Chen et al.
---
Most existing person re-identification (ReID) methods have good feature
representations to distinguish pedestrians with deep convolutional neural
network (CNN) and metric learning methods. However, these works concentrate on
the similarity between encoder output and ground-truth, ignoring the
correlation between input and encoder output, which affects the performance of
identifying different pedestrians. To address this limitation, We design a Deep
InfoMax (DIM) network to maximize the mutual information (MI) between the input
image and encoder output, which doesn't need any auxiliary labels. To evaluate
the effectiveness of the DIM network, we propose end-to-end Global-DIM and
Local-DIM models. Additionally, the DIM network provides a new solution for
cross-dataset unsupervised ReID issue as it needs no extra labels. The
experiments prove the superiority of MI theory on the ReID issue, which
achieves the state-of-the-art results.