---
layout: publication
title: Object-level Representation Learning For Few-shot Image Classification
authors: Liangqu Long, Wei Wang, Jun Wen, Meihui Zhang, Qian Lin, Beng Chin Ooi
conference: Arxiv
year: 2018
bibkey: long2018object
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.10777'}]
tags: [Datasets, Few-shot & Zero-shot]
short_authors: Long et al.
---
Few-shot learning that trains image classifiers over few labeled examples per
category is a challenging task. In this paper, we propose to exploit an
additional big dataset with different categories to improve the accuracy of
few-shot learning over our target dataset. Our approach is based on the
observation that images can be decomposed into objects, which may appear in
images from both the additional dataset and our target dataset. We use the
object-level relation learned from the additional dataset to infer the
similarity of images in our target dataset with unseen categories. Nearest
neighbor search is applied to do image classification, which is a
non-parametric model and thus does not need fine-tuning. We evaluate our
algorithm on two popular datasets, namely Omniglot and MiniImagenet. We obtain
8.5% and 2.7% absolute improvements for 5-way 1-shot and 5-way 5-shot
experiments on MiniImagenet, respectively. Source code will be published upon
acceptance.