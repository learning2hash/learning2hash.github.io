---
layout: publication
title: Unsupervised Person Re-identification Via Softened Similarity Learning
authors: Yutian Lin, Lingxi Xie, Yu Wu, Chenggang Yan, Qi Tian
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: lin2020unsupervised
citations: 282
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.03547'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Lin et al.
---
Person re-identification (re-ID) is an important topic in computer vision.
This paper studies the unsupervised setting of re-ID, which does not require
any labeled information and thus is freely deployed to new scenarios. There are
very few studies under this setting, and one of the best approach till now used
iterative clustering and classification, so that unlabeled images are clustered
into pseudo classes for a classifier to get trained, and the updated features
are used for clustering and so on. This approach suffers two problems, namely,
the difficulty of determining the number of clusters, and the hard quantization
loss in clustering. In this paper, we follow the iterative training mechanism
but discard clustering, since it incurs loss from hard quantization, yet its
only product, image-level similarity, can be easily replaced by pairwise
computation and a softened classification task. With these improvements, our
approach becomes more elegant and is more robust to hyper-parameter changes.
Experiments on two image-based and video-based datasets demonstrate
state-of-the-art performance under the unsupervised re-ID setting.