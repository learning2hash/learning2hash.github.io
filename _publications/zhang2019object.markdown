---
layout: publication
title: Object Discovery From A Single Unlabeled Image By Mining Frequent Itemset With
  Multi-scale Features
authors: Runsheng Zhang, Yaping Huang, Mengyang Pu, Jian Zhang, Qingji Guan, Qi Zou,
  Haibin Ling
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: zhang2019object
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.09968'}]
tags: ["Unsupervised"]
short_authors: Zhang et al.
---
TThe goal of our work is to discover dominant objects in a very general
setting where only a single unlabeled image is given. This is far more
challenge than typical co-localization or weakly-supervised localization tasks.
To tackle this problem, we propose a simple but effective pattern mining-based
method, called Object Location Mining (OLM), which exploits the advantages of
data mining and feature representation of pre-trained convolutional neural
networks (CNNs). Specifically, we first convert the feature maps from a
pre-trained CNN model into a set of transactions, and then discovers frequent
patterns from transaction database through pattern mining techniques. We
observe that those discovered patterns, i.e., co-occurrence highlighted
regions, typically hold appearance and spatial consistency. Motivated by this
observation, we can easily discover and localize possible objects by merging
relevant meaningful patterns. Extensive experiments on a variety of benchmarks
demonstrate that OLM achieves competitive localization performance compared
with the state-of-the-art methods. We also evaluate our approach compared with
unsupervised saliency detection methods and achieves competitive results on
seven benchmark datasets. Moreover, we conduct experiments on fine-grained
classification to show that our proposed method can locate the entire object
and parts accurately, which can benefit to improving the classification results
significantly.