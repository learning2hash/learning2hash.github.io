---
layout: publication
title: 'Neural Networks Behave As Hash Encoders: An Empirical Study'
authors: Fengxiang He, Shiye Lei, Jianmin Ji, Dacheng Tao
conference: Arxiv
year: 2021
bibkey: he2021neural
citations: 1
additional_links: [{name: Code, url: 'https://github.com/LeavesLei/activation-code'},
  {name: Paper, url: 'https://arxiv.org/abs/2101.05490'}]
tags: ["Evaluation", "Neural Hashing"]
short_authors: He et al.
---
The input space of a neural network with ReLU-like activations is partitioned
into multiple linear regions, each corresponding to a specific activation
pattern of the included ReLU-like activations. We demonstrate that this
partition exhibits the following encoding properties across a variety of deep
learning models: (1) \{\it determinism\}: almost every linear region contains at
most one training example. We can therefore represent almost every training
example by a unique activation pattern, which is parameterized by a \{\it neural
code\}; and (2) \{\it categorization\}: according to the neural code, simple
algorithms, such as \(K\)-Means, \(K\)-NN, and logistic regression, can achieve
fairly good performance on both training and test data. These encoding
properties surprisingly suggest that \{\it normal neural networks well-trained
for classification behave as hash encoders without any extra efforts.\} In
addition, the encoding properties exhibit variability in different scenarios.
\{Further experiments demonstrate that \{\it model size\}, \{\it training time\},
\{\it training sample size\}, \{\it regularization\}, and \{\it label noise\}
contribute in shaping the encoding properties, while the impacts of the first
three are dominant.\} We then define an \{\it activation hash phase chart\} to
represent the space expanded by \{model size\}, training time, training sample
size, and the encoding properties, which is divided into three canonical
regions: \{\it under-expressive regime\}, \{\it critically-expressive regime\}, and
\{\it sufficiently-expressive regime\}. The source code package is available at
https://github.com/LeavesLei/activation-code.