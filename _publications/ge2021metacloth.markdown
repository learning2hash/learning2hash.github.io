---
layout: publication
title: 'Metacloth: Learning Unseen Tasks Of Dense Fashion Landmark Detection From
  A Few Samples'
authors: Yuying Ge, Ruimao Zhang, Ping Luo
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: ge2021metacloth
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.02763'}]
tags: []
short_authors: Yuying Ge, Ruimao Zhang, Ping Luo
---
Recent advanced methods for fashion landmark detection are mainly driven by
training convolutional neural networks on large-scale fashion datasets, which
has a large number of annotated landmarks. However, such large-scale
annotations are difficult and expensive to obtain in real-world applications,
thus models that can generalize well from a small amount of labelled data are
desired. We investigate this problem of few-shot fashion landmark detection,
where only a few labelled samples are available for an unseen task. This work
proposes a novel framework named MetaCloth via meta-learning, which is able to
learn unseen tasks of dense fashion landmark detection with only a few
annotated samples. Unlike previous meta-learning work that focus on solving
"N-way K-shot" tasks, where each task predicts N number of classes by training
with K annotated samples for each class (N is fixed for all seen and unseen
tasks), a task in MetaCloth detects N different landmarks for different
clothing categories using K samples, where N varies across tasks, because
different clothing categories usually have various number of landmarks.
Therefore, numbers of parameters are various for different seen and unseen
tasks in MetaCloth. MetaCloth is carefully designed to dynamically generate
different numbers of parameters for different tasks, and learn a generalizable
feature extraction network from a few annotated samples with a set of good
initialization parameters. Extensive experiments show that MetaCloth
outperforms its counterparts by a large margin.