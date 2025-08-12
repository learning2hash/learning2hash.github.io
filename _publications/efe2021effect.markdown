---
layout: publication
title: Effect Of Parameter Optimization On Classical And Learning-based Image Matching
  Methods
authors: Ufuk Efe, Kutalmis Gokalp Ince, A. Aydin Alatan
conference: 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2021
bibkey: efe2021effect
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08179'}]
tags: ["ICCV"]
short_authors: Ufuk Efe, Kutalmis Gokalp Ince, A. Aydin Alatan
---
Deep learning-based image matching methods are improved significantly during
the recent years. Although these methods are reported to outperform the
classical techniques, the performance of the classical methods is not examined
in detail. In this study, we compare classical and learning-based methods by
employing mutual nearest neighbor search with ratio test and optimizing the
ratio test threshold to achieve the best performance on two different
performance metrics. After a fair comparison, the experimental results on
HPatches dataset reveal that the performance gap between classical and
learning-based methods is not that significant. Throughout the experiments, we
demonstrated that SuperGlue is the state-of-the-art technique for the image
matching problem on HPatches dataset. However, if a single parameter, namely
ratio test threshold, is carefully optimized, a well-known traditional method
SIFT performs quite close to SuperGlue and even outperforms in terms of mean
matching accuracy (MMA) under 1 and 2 pixel thresholds. Moreover, a recent
approach, DFM, which only uses pre-trained VGG features as descriptors and
ratio test, is shown to outperform most of the well-trained learning-based
methods. Therefore, we conclude that the parameters of any classical method
should be analyzed carefully before comparing against a learning-based
technique.