---
layout: publication
title: Discovering Underlying Person Structure Pattern With Relative Local Distance
  For Person Re-identification
authors: Guangcong Wang, Jianhuang Lai, Zhenyu Xie, Xiaohua Xie
conference: Arxiv
year: 2019
bibkey: wang2019discovering
citations: 5
additional_links: [{name: Code, url: 'https://github.com/Wanggcong/RLD_codes'}, {
    name: Paper, url: 'https://arxiv.org/abs/1901.10100'}]
tags: []
short_authors: Wang et al.
---
Modeling the underlying person structure for person re-identification (re-ID)
is difficult due to diverse deformable poses, changeable camera views and
imperfect person detectors. How to exploit underlying person structure
information without extra annotations to improve the performance of person
re-ID remains largely unexplored. To address this problem, we propose a novel
Relative Local Distance (RLD) method that integrates a relative local distance
constraint into convolutional neural networks (CNNs) in an end-to-end way. It
is the first time that the relative local constraint is proposed to guide the
global feature representation learning. Specially, a relative local distance
matrix is computed by using feature maps and then regarded as a regularizer to
guide CNNs to learn a structure-aware feature representation. With the
discovered underlying person structure, the RLD method builds a bridge between
the global and local feature representation and thus improves the capacity of
feature representation for person re-ID. Furthermore, RLD also significantly
accelerates deep network training compared with conventional methods. The
experimental results show the effectiveness of RLD on the CUHK03, Market-1501,
and DukeMTMC-reID datasets. Code is available at
https://github.com/Wanggcong/RLD_codes.