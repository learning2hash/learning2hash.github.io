---
layout: publication
title: 'Bsnet: Bi-similarity Network For Few-shot Fine-grained Image Classification'
authors: Xiaoxu Li, Jijie Wu, Zhuo Sun, Zhanyu Ma, Jie Cao, Jing-Hao Xue
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: li2020bsnet
citations: 141
additional_links: [{name: Code, url: 'https://github.com/spraise/BSNet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2011.14311'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Few-shot learning for fine-grained image classification has gained recent
attention in computer vision. Among the approaches for few-shot learning, due
to the simplicity and effectiveness, metric-based methods are favorably
state-of-the-art on many tasks. Most of the metric-based methods assume a
single similarity measure and thus obtain a single feature space. However, if
samples can simultaneously be well classified via two distinct similarity
measures, the samples within a class can distribute more compactly in a smaller
feature space, producing more discriminative feature maps. Motivated by this,
we propose a so-called \textit\{Bi-Similarity Network\} (\textit\{BSNet\}) that
consists of a single embedding module and a bi-similarity module of two
similarity measures. After the support images and the query images pass through
the convolution-based embedding module, the bi-similarity module learns feature
maps according to two similarity measures of diverse characteristics. In this
way, the model is enabled to learn more discriminative and less
similarity-biased features from few shots of fine-grained images, such that the
model generalization ability can be significantly improved. Through extensive
experiments by slightly modifying established metric/similarity based networks,
we show that the proposed approach produces a substantial improvement on
several fine-grained image benchmark datasets. Codes are available at:
https://github.com/spraise/BSNet