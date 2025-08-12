---
layout: publication
title: Weak-shot Fine-grained Classification Via Similarity Transfer
authors: Junjie Chen, Li Niu, Liu Liu, Liqing Zhang
conference: Arxiv
year: 2020
bibkey: chen2020weak
citations: 8
additional_links: [{name: Code, url: 'https://github.com/bcmi/SimTrans-Weak-Shot-Classification'},
  {name: Paper, url: 'https://arxiv.org/abs/2009.09197'}]
tags: []
short_authors: Chen et al.
---
Recognizing fine-grained categories remains a challenging task, due to the
subtle distinctions among different subordinate categories, which results in
the need of abundant annotated samples. To alleviate the data-hungry problem,
we consider the problem of learning novel categories from web data with the
support of a clean set of base categories, which is referred to as weak-shot
learning. In this setting, we propose a method called SimTrans to transfer
pairwise semantic similarity from base categories to novel categories.
Specifically, we firstly train a similarity net on clean data, and then
leverage the transferred similarity to denoise web training data using two
simple yet effective strategies. In addition, we apply adversarial loss on
similarity net to enhance the transferability of similarity. Comprehensive
experiments demonstrate the effectiveness of our weak-shot setting and our
SimTrans method. Datasets and codes are available at
https://github.com/bcmi/SimTrans-Weak-Shot-Classification.