---
layout: publication
title: 'Deepfirearm: Learning Discriminative Feature Representation For Fine-grained
  Firearm Retrieval'
authors: Jiedong Hao, Jing Dong, Wei Wang, Tieniu Tan
conference: 2018 24th International Conference on Pattern Recognition (ICPR)
year: 2018
bibkey: hao2018deepfirearm
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.02984'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Hao et al.
---
There are great demands for automatically regulating inappropriate appearance
of shocking firearm images in social media or identifying firearm types in
forensics. Image retrieval techniques have great potential to solve these
problems. To facilitate research in this area, we introduce Firearm 14k, a
large dataset consisting of over 14,000 images in 167 categories. It can be
used for both fine-grained recognition and retrieval of firearm images. Recent
advances in image retrieval are mainly driven by fine-tuning state-of-the-art
convolutional neural networks for retrieval task. The conventional single
margin contrastive loss, known for its simplicity and good performance, has
been widely used. We find that it performs poorly on the Firearm 14k dataset
due to: (1) Loss contributed by positive and negative image pairs is unbalanced
during training process. (2) A huge domain gap exists between this dataset and
ImageNet. We propose to deal with the unbalanced loss by employing a double
margin contrastive loss. We tackle the domain gap issue with a two-stage
training strategy, where we first fine-tune the network for classification, and
then fine-tune it for retrieval. Experimental results show that our approach
outperforms the conventional single margin approach by a large margin (up to
88.5% relative improvement) and even surpasses the strong triplet-loss-based
approach.