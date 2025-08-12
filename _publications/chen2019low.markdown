---
layout: publication
title: Low-rank Discriminative Least Squares Regression For Image Classification
authors: Zhe Chen, Xiao-jun Wu, Josef Kittler
conference: Signal Processing
year: 2020
bibkey: chen2019low
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.07832'}]
tags: ["Evaluation"]
short_authors: Zhe Chen, Xiao-jun Wu, Josef Kittler
---
Latest least squares regression (LSR) methods mainly try to learn slack
regression targets to replace strict zero-one labels. However, the difference
of intra-class targets can also be highlighted when enlarging the distance
between different classes, and roughly persuing relaxed targets may lead to the
problem of overfitting. To solve above problems, we propose a low-rank
discriminative least squares regression model (LRDLSR) for multi-class image
classification. Specifically, LRDLSR class-wisely imposes low-rank constraint
on the intra-class regression targets to encourage its compactness and
similarity. Moreover, LRDLSR introduces an additional regularization term on
the learned targets to avoid the problem of overfitting. These two improvements
are helpful to learn a more discriminative projection for regression and thus
achieving better classification performance. Experimental results over a range
of image databases demonstrate the effectiveness of the proposed LRDLSR method.