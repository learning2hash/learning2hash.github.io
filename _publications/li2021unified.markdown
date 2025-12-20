---
layout: publication
title: Unified Batch All Triplet Loss For Visible-infrared Person Re-identification
authors: Wenkang Li, Ke Qi, Wenbin Chen, Yicong Zhou
conference: 2021 International Joint Conference on Neural Networks (IJCNN)
year: 2021
bibkey: li2021unified
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04607'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Li et al.
---
Visible-Infrared cross-modality person re-identification (VI-ReID), whose aim
is to match person images between visible and infrared modality, is a
challenging cross-modality image retrieval task. Batch Hard Triplet loss is
widely used in person re-identification tasks, but it does not perform well in
the Visible-Infrared person re-identification task. Because it only optimizes
the hardest triplet for each anchor image within the mini-batch, samples in the
hardest triplet may all belong to the same modality, which will lead to the
imbalance problem of modality optimization. To address this problem, we adopt
the batch all triplet selection strategy, which selects all the possible
triplets among samples to optimize instead of the hardest triplet. Furthermore,
we introduce Unified Batch All Triplet loss and Cosine Softmax loss to
collaboratively optimize the cosine distance between image vectors. Similarly,
we rewrite the Hetero Center Triplet loss, which is proposed for VI-ReID task,
into a batch all form to improve model performance. Extensive experiments
indicate the effectiveness of the proposed methods, which outperform
state-of-the-art methods by a wide margin.