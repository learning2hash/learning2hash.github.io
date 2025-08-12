---
layout: publication
title: Discriminative Sample-guided And Parameter-efficient Feature Space Adaptation
  For Cross-domain Few-shot Learning
authors: Rashindrie Perera, Saman Halgamuge
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: perera2024discriminative
citations: 4
additional_links: [{name: Code, url: 'https://github.com/rashindrie/DIPA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2403.04492'}]
tags: ["CVPR"]
short_authors: Rashindrie Perera, Saman Halgamuge
---
In this paper, we look at cross-domain few-shot classification which presents
the challenging task of learning new classes in previously unseen domains with
few labelled examples. Existing methods, though somewhat effective, encounter
several limitations, which we alleviate through two significant improvements.
First, we introduce a lightweight parameter-efficient adaptation strategy to
address overfitting associated with fine-tuning a large number of parameters on
small datasets. This strategy employs a linear transformation of pre-trained
features, significantly reducing the trainable parameter count. Second, we
replace the traditional nearest centroid classifier with a discriminative
sample-aware loss function, enhancing the model's sensitivity to the inter- and
intra-class variances within the training set for improved clustering in
feature space. Empirical evaluations on the Meta-Dataset benchmark showcase
that our approach not only improves accuracy up to 7.7% and 5.3% on
previously seen and unseen datasets, respectively, but also achieves the above
performance while being at least \(\sim3\times\) more parameter-efficient than
existing methods, establishing a new state-of-the-art in cross-domain few-shot
learning. Our code is available at https://github.com/rashindrie/DIPA.