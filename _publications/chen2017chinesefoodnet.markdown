---
layout: publication
title: 'Chinesefoodnet: A Large-scale Image Dataset For Chinese Food Recognition'
authors: Xin Chen, Yu Zhu, Hua Zhou, Liang Diao, Dongyan Wang
conference: Arxiv
year: 2017
bibkey: chen2017chinesefoodnet
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02743'}]
tags: ["Datasets"]
short_authors: Chen et al.
---
In this paper, we introduce a new and challenging large-scale food image
dataset called "ChineseFoodNet", which aims to automatically recognizing
pictured Chinese dishes. Most of the existing food image datasets collected
food images either from recipe pictures or selfie. In our dataset, images of
each food category of our dataset consists of not only web recipe and menu
pictures but photos taken from real dishes, recipe and menu as well.
ChineseFoodNet contains over 180,000 food photos of 208 categories, with each
category covering a large variations in presentations of same Chinese food. We
present our efforts to build this large-scale image dataset, including food
category selection, data collection, and data clean and label, in particular
how to use machine learning methods to reduce manual labeling work that is an
expensive process. We share a detailed benchmark of several state-of-the-art
deep convolutional neural networks (CNNs) on ChineseFoodNet. We further propose
a novel two-step data fusion approach referred as "TastyNet", which combines
prediction results from different CNNs with voting method. Our proposed
approach achieves top-1 accuracies of 81.43% on the validation set and 81.55%
on the test set, respectively. The latest dataset is public available for
research and can be achieved at https://sites.google.com/view/chinesefoodnet.