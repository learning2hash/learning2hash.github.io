---
layout: publication
title: 'Seeing The Big Picture: Deep Embedding With Contextual Evidences'
authors: Liang Zheng, Shengjin Wang, Fei He, Qi Tian
conference: "Arxiv"
year: 2014
citations: 16
bibkey: zheng2014seeing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1406.0132'}
tags: ['Cross-Modal', 'Deep', 'Retrieval Models', 'Datasets', 'Supervised', 'Applications']
---
In the Bag-of-Words (BoW) model based image retrieval task, the precision of
visual matching plays a critical role in improving retrieval performance.
Conventionally, local cues of a keypoint are employed. However, such strategy
does not consider the contextual evidences of a keypoint, a problem which would
lead to the prevalence of false matches. To address this problem, this paper
defines "true match" as a pair of keypoints which are similar on three levels,
i.e., local, regional, and global. Then, a principled probabilistic framework
is established, which is capable of implicitly integrating discriminative cues
from all these feature levels.
  Specifically, the Convolutional Neural Network (CNN) is employed to extract
features from regional and global patches, leading to the so-called "Deep
Embedding" framework. CNN has been shown to produce excellent performance on a
dozen computer vision tasks such as image classification and detection, but few
works have been done on BoW based image retrieval. In this paper, firstly we
show that proper pre-processing techniques are necessary for effective usage of
CNN feature. Then, in the attempt to fit it into our model, a novel indexing
structure called "Deep Indexing" is introduced, which dramatically reduces
memory usage.
  Extensive experiments on three benchmark datasets demonstrate that, the
proposed Deep Embedding method greatly promotes the retrieval accuracy when CNN
feature is integrated. We show that our method is efficient in terms of both
memory and time cost, and compares favorably with the state-of-the-art methods.
