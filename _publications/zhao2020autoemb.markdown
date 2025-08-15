---
layout: publication
title: 'Autoemb: Automated Embedding Dimensionality Search In Streaming Recommendations'
authors: Xiangyu Zhao, Chong Wang, Ming Chen, Xudong Zheng, Xiaobing Liu, Jiliang
  Tang
conference: 2021 IEEE International Conference on Data Mining (ICDM)
year: 2021
bibkey: zhao2020autoemb
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11252'}]
tags: ["Datasets", "Evaluation", "Recommender Systems"]
short_authors: Zhao et al.
---
Deep learning based recommender systems (DLRSs) often have embedding layers,
which are utilized to lessen the dimensionality of categorical variables (e.g.
user/item identifiers) and meaningfully transform them in the low-dimensional
space. The majority of existing DLRSs empirically pre-define a fixed and
unified dimension for all user/item embeddings. It is evident from recent
researches that different embedding sizes are highly desired for different
users/items according to their popularity. However, manually selecting
embedding sizes in recommender systems can be very challenging due to the large
number of users/items and the dynamic nature of their popularity. Thus, in this
paper, we propose an AutoML based end-to-end framework (AutoEmb), which can
enable various embedding dimensions according to the popularity in an automated
and dynamic manner. To be specific, we first enhance a typical DLRS to allow
various embedding dimensions; then we propose an end-to-end differentiable
framework that can automatically select different embedding dimensions
according to user/item popularity; finally we propose an AutoML based
optimization algorithm in a streaming recommendation setting. The experimental
results based on widely used benchmark datasets demonstrate the effectiveness
of the AutoEmb framework.