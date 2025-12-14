---
layout: publication
title: 'Foresthash: Semantic Hashing With Shallow Random Forests And Tiny Convolutional
  Networks'
authors: Qiang Qiu, Jose Lezama, Alex Bronstein, Guillermo Sapiro
conference: Arxiv
year: 2017
bibkey: qiu2017foresthash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08364'}]
tags: [Image Retrieval, Neural Hashing, Datasets, Scalability, Hashing Methods]
short_authors: Qiu et al.
---
Hash codes are efficient data representations for coping with the ever
growing amounts of data. In this paper, we introduce a random forest semantic
hashing scheme that embeds tiny convolutional neural networks (CNN) into
shallow random forests, with near-optimal information-theoretic code
aggregation among trees. We start with a simple hashing scheme, where random
trees in a forest act as hashing functions by setting `1' for the visited tree
leaf, and `0' for the rest. We show that traditional random forests fail to
generate hashes that preserve the underlying similarity between the trees,
rendering the random forests approach to hashing challenging. To address this,
we propose to first randomly group arriving classes at each tree split node
into two groups, obtaining a significantly simplified two-class classification
problem, which can be handled using a light-weight CNN weak learner. Such
random class grouping scheme enables code uniqueness by enforcing each class to
share its code with different classes in different trees. A non-conventional
low-rank loss is further adopted for the CNN weak learners to encourage code
consistency by minimizing intra-class variations and maximizing inter-class
distance for the two random class groups. Finally, we introduce an
information-theoretic approach for aggregating codes of individual trees into a
single hash code, producing a near-optimal unique hash for each class. The
proposed approach significantly outperforms state-of-the-art hashing methods
for image retrieval tasks on large-scale public datasets, while performing at
the level of other state-of-the-art image classification techniques while
utilizing a more compact and efficient scalable representation. This work
proposes a principled and robust procedure to train and deploy in parallel an
ensemble of light-weight CNNs, instead of simply going deeper.