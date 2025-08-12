---
layout: publication
title: 'Cross-label Suppression: A Discriminative And Fast Dictionary Learning With
  Group Regularization'
authors: Xiudong Wang, Yuantao Gu
conference: IEEE Transactions on Image Processing
year: 2017
bibkey: wang2017cross
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02928'}]
tags: ["Efficiency"]
short_authors: Xiudong Wang, Yuantao Gu
---
This paper addresses image classification through learning a compact and
discriminative dictionary efficiently. Given a structured dictionary with each
atom (columns in the dictionary matrix) related to some label, we propose
cross-label suppression constraint to enlarge the difference among
representations for different classes. Meanwhile, we introduce group
regularization to enforce representations to preserve label properties of
original samples, meaning the representations for the same class are encouraged
to be similar. Upon the cross-label suppression, we don't resort to
frequently-used \(\ell_0\)-norm or \(\ell_1\)-norm for coding, and obtain
computational efficiency without losing the discriminative power for
categorization. Moreover, two simple classification schemes are also developed
to take full advantage of the learnt dictionary. Extensive experiments on six
data sets including face recognition, object categorization, scene
classification, texture recognition and sport action categorization are
conducted, and the results show that the proposed approach can outperform lots
of recently presented dictionary algorithms on both recognition accuracy and
computational efficiency.