---
layout: publication
title: 'Imbalanced Malware Images Classification: A CNN Based Approach'
authors: Songqing Yue, Tianyang Wang
conference: Arxiv
year: 2017
bibkey: yue2017imbalanced
citations: 108
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.08042'}]
tags: []
short_authors: Songqing Yue, Tianyang Wang
---
Deep convolutional neural networks (CNNs) can be applied to malware binary
detection via image classification. The performance, however, is degraded due
to the imbalance of malware families (classes). To mitigate this issue, we
propose a simple yet effective weighted softmax loss which can be employed as
the final layer of deep CNNs. The original softmax loss is weighted, and the
weight value can be determined according to class size. A scaling parameter is
also included in computing the weight. Proper selection of this parameter is
studied and an empirical option is suggested. The weighted loss aims at
alleviating the impact of data imbalance in an end-to-end learning fashion. To
validate the efficacy, we deploy the proposed weighted loss in a pre-trained
deep CNN model and fine-tune it to achieve promising results on malware images
classification. Extensive experiments also demonstrate that the new loss
function can well fit other typical CNNs, yielding an improved classification
performance.