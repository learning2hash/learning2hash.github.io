---
layout: publication
title: 'Making Online Sketching Hashing Even Faster'
authors: Xixian Chen, Haiqin Yang, Shenglin Zhao, Michael R. Lyu, Irwin King
conference: "IEEE Transactions on Knowledge and Data Engineering 2019"
year: 2020
citations: 13
bibkey: chen2020making
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2010.04948'}
tags: ['Cross-Modal', 'Independent', 'Efficiency', 'Shallow', 'Datasets', 'Training Strategy', 'Hashing', 'Applications']
---
Data-dependent hashing methods have demonstrated good performance in various
machine learning applications to learn a low-dimensional representation from
the original data. However, they still suffer from several obstacles: First,
most of existing hashing methods are trained in a batch mode, yielding
inefficiency for training streaming data. Second, the computational cost and
the memory consumption increase extraordinarily in the big data setting, which
perplexes the training procedure. Third, the lack of labeled data hinders the
improvement of the model performance. To address these difficulties, we utilize
online sketching hashing (OSH) and present a FasteR Online Sketching Hashing
(FROSH) algorithm to sketch the data in a more compact form via an independent
transformation. We provide theoretical justification to guarantee that our
proposed FROSH consumes less time and achieves a comparable sketching precision
under the same memory cost of OSH. We also extend FROSH to its distributed
implementation, namely DFROSH, to further reduce the training time cost of
FROSH while deriving the theoretical bound of the sketching precision. Finally,
we conduct extensive experiments on both synthetic and real datasets to
demonstrate the attractive merits of FROSH and DFROSH.
