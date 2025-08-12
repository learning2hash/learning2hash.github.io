---
layout: publication
title: 'Simpleshot: Revisiting Nearest-neighbor Classification For Few-shot Learning'
authors: Yan Wang, Wei-Lun Chao, Kilian Q. Weinberger, Laurens van Der Maaten
conference: Arxiv
year: 2019
bibkey: wang2019simpleshot
citations: 242
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.04623'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Few-shot learners aim to recognize new object classes based on a small number
of labeled training examples. To prevent overfitting, state-of-the-art few-shot
learners use meta-learning on convolutional-network features and perform
classification using a nearest-neighbor classifier. This paper studies the
accuracy of nearest-neighbor baselines without meta-learning. Surprisingly, we
find simple feature transformations suffice to obtain competitive few-shot
learning accuracies. For example, we find that a nearest-neighbor classifier
used in combination with mean-subtraction and L2-normalization outperforms
prior results in three out of five settings on the miniImageNet dataset.