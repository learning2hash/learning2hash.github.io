---
layout: publication
title: Weakly Supervised Learning With Side Information For Noisy Labeled Images
authors: Lele Cheng, Xiangzeng Zhou, Liming Zhao, Dangwei Li, Hong Shang, Yun Zheng,
  Pan Pan, Yinghui Xu
conference: Lecture Notes in Computer Science
year: 2020
bibkey: cheng2020weakly
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.11586'}]
tags: ["Supervised"]
short_authors: Cheng et al.
---
In many real-world datasets, like WebVision, the performance of DNN based
classifier is often limited by the noisy labeled data. To tackle this problem,
some image related side information, such as captions and tags, often reveal
underlying relationships across images. In this paper, we present an efficient
weakly supervised learning by using a Side Information Network (SINet), which
aims to effectively carry out a large scale classification with severely noisy
labels. The proposed SINet consists of a visual prototype module and a noise
weighting module. The visual prototype module is designed to generate a compact
representation for each category by introducing the side information. The noise
weighting module aims to estimate the correctness of each noisy image and
produce a confidence score for image ranking during the training procedure. The
propsed SINet can largely alleviate the negative impact of noisy image labels,
and is beneficial to train a high performance CNN based classifier. Besides, we
released a fine-grained product dataset called AliProducts, which contains more
than 2.5 million noisy web images crawled from the internet by using queries
generated from 50,000 fine-grained semantic classes. Extensive experiments on
several popular benchmarks (i.e. Webvision, ImageNet and Clothing-1M) and our
proposed AliProducts achieve state-of-the-art performance. The SINet has won
the first place in the classification task on WebVision Challenge 2019, and
outperformed other competitors by a large margin.