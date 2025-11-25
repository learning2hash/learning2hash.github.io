---
layout: publication
title: 'Augnet: End-to-end Unsupervised Visual Representation Learning With Image
  Augmentation'
authors: Mingxiang Chen, Zhanguo Chang, Haonan Lu, Bitao Yang, Zhuang Li, Liufang
  Guo, Zhecheng Wang
conference: Arxiv
year: 2021
bibkey: chen2021augnet
citations: 7
additional_links: [{name: Code, url: 'https://github.com/chenmingxiang110/AugNet'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.06250'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Unsupervised"]
short_authors: Chen et al.
---
Most of the achievements in artificial intelligence so far were accomplished
by supervised learning which requires numerous annotated training data and thus
costs innumerable manpower for labeling. Unsupervised learning is one of the
effective solutions to overcome such difficulties. In our work, we propose
AugNet, a new deep learning training paradigm to learn image features from a
collection of unlabeled pictures. We develop a method to construct the
similarities between pictures as distance metrics in the embedding space by
leveraging the inter-correlation between augmented versions of samples. Our
experiments demonstrate that the method is able to represent the image in low
dimensional space and performs competitively in downstream tasks such as image
classification and image similarity comparison. Specifically, we achieved over
60% and 27% accuracy on the STL10 and CIFAR100 datasets with unsupervised
clustering, respectively. Moreover, unlike many deep-learning-based image
retrieval algorithms, our approach does not require access to external
annotated datasets to train the feature extractor, but still shows comparable
or even better feature representation ability and easy-to-use characteristics.
In our evaluations, the method outperforms all the state-of-the-art image
retrieval algorithms on some out-of-domain image datasets. The code for the
model implementation is available at
https://github.com/chenmingxiang110/AugNet.