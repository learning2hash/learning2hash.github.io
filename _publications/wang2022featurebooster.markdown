---
layout: publication
title: 'Featurebooster: Boosting Feature Descriptors With A Lightweight Neural Network'
authors: Xinjiang Wang, Zeyu Liu, Yu Hu, Wei Xi, Wenxian Yu, Danping Zou
conference: Arxiv
year: 2022
bibkey: wang2022featurebooster
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.15069'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Wang et al.
---
We introduce a lightweight network to improve descriptors of keypoints within
the same image. The network takes the original descriptors and the geometric
properties of keypoints as the input, and uses an MLP-based self-boosting stage
and a Transformer-based cross-boosting stage to enhance the descriptors. The
boosted descriptors can be either real-valued or binary ones. We use the
proposed network to boost both hand-crafted (ORB, SIFT) and the
state-of-the-art learning-based descriptors (SuperPoint, ALIKE) and evaluate
them on image matching, visual localization, and structure-from-motion tasks.
The results show that our method significantly improves the performance of each
task, particularly in challenging cases such as large illumination changes or
repetitive patterns. Our method requires only 3.2ms on desktop GPU and 27ms on
embedded GPU to process 2000 features, which is fast enough to be applied to a
practical system. The code and trained weights are publicly available at
github.com/SJTU-ViSYS/FeatureBooster.