---
layout: publication
title: Visual Search At Ebay
authors: Fan Yang, Ajinkya Kale, Yury Bubnov, Leon Stein, Qiaosong Wang, Hadi Kiapour,
  Robinson Piramuthu
conference: Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge
  Discovery and Data Mining
year: 2017
bibkey: yang2017visual
citations: 116
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.03154'}]
tags: [Evaluation, Supervised, Image Retrieval, Neural Hashing, Datasets, Scalability,
  Unsupervised, KDD]
short_authors: Yang et al.
---
In this paper, we propose a novel end-to-end approach for scalable visual
search infrastructure. We discuss the challenges we faced for a massive
volatile inventory like at eBay and present our solution to overcome those. We
harness the availability of large image collection of eBay listings and
state-of-the-art deep learning techniques to perform visual search at scale.
Supervised approach for optimized search limited to top predicted categories
and also for compact binary signature are key to scale up without compromising
accuracy and precision. Both use a common deep neural network requiring only a
single forward inference. The system architecture is presented with in-depth
discussions of its basic components and optimizations for a trade-off between
search relevance and latency. This solution is currently deployed in a
distributed cloud infrastructure and fuels visual search in eBay ShopBot and
Close5. We show benchmark on ImageNet dataset on which our approach is faster
and more accurate than several unsupervised baselines. We share our learnings
with the hope that visual search becomes a first class citizen for all large
scale search engines rather than an afterthought.