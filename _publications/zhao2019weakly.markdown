---
layout: publication
title: A weakly supervised adaptive triplet loss for deep metric learning
authors: Zhao et al.
conference: 2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)
year: 2019
bibkey: zhao2019weakly
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.12939'}]
tags: [ICCV, Distance Metric Learning, Supervised]
---
We address the problem of distance metric learning in visual similarity
search, defined as learning an image embedding model which projects images into
Euclidean space where semantically and visually similar images are closer and
dissimilar images are further from one another. We present a weakly supervised
adaptive triplet loss (ATL) capable of capturing fine-grained semantic
similarity that encourages the learned image embedding models to generalize
well on cross-domain data. The method uses weakly labeled product description
data to implicitly determine fine grained semantic classes, avoiding the need
to annotate large amounts of training data. We evaluate on the Amazon fashion
retrieval benchmark and DeepFashion in-shop retrieval data. The method boosts
the performance of triplet loss baseline by 10.6% on cross-domain data and
out-performs the state-of-art model on all evaluation metrics.