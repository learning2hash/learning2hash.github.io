---
layout: publication
title: Few-shot Object Detection With Fully Cross-transformer
authors: Guangxing Han, Jiawei Ma, Shiyuan Huang, Long Chen, Shih-Fu Chang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: han2022few
citations: 126
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15021'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Han et al.
---
Few-shot object detection (FSOD), with the aim to detect novel objects using
very few training examples, has recently attracted great research interest in
the community. Metric-learning based methods have been demonstrated to be
effective for this task using a two-branch based siamese network, and calculate
the similarity between image regions and few-shot examples for detection.
However, in previous works, the interaction between the two branches is only
restricted in the detection head, while leaving the remaining hundreds of
layers for separate feature extraction. Inspired by the recent work on vision
transformers and vision-language transformers, we propose a novel Fully
Cross-Transformer based model (FCT) for FSOD by incorporating cross-transformer
into both the feature backbone and detection head. The asymmetric-batched
cross-attention is proposed to aggregate the key information from the two
branches with different batch sizes. Our model can improve the few-shot
similarity learning between the two branches by introducing the multi-level
interactions. Comprehensive experiments on both PASCAL VOC and MSCOCO FSOD
benchmarks demonstrate the effectiveness of our model.