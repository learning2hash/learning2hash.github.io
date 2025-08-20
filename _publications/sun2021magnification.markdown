---
layout: publication
title: Magnification-independent Histopathological Image Classification With Similarity-based
  Multi-scale Embeddings
authors: Yibao Sun, Xingru Huang, Yaqi Wang, Huiyu Zhou, Qianni Zhang
conference: Arxiv
year: 2021
bibkey: sun2021magnification
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.01063'}]
tags: [Evaluation, Distance Metric Learning, Datasets]
short_authors: Sun et al.
---
The classification of histopathological images is of great value in both
cancer diagnosis and pathological studies. However, multiple reasons, such as
variations caused by magnification factors and class imbalance, make it a
challenging task where conventional methods that learn from image-label
datasets perform unsatisfactorily in many cases. We observe that tumours of the
same class often share common morphological patterns. To exploit this fact, we
propose an approach that learns similarity-based multi-scale embeddings (SMSE)
for magnification-independent histopathological image classification. In
particular, a pair loss and a triplet loss are leveraged to learn
similarity-based embeddings from image pairs or image triplets. The learned
embeddings provide accurate measurements of similarities between images, which
are regarded as a more effective form of representation for histopathological
morphology than normal image features. Furthermore, in order to ensure the
generated models are magnification-independent, images acquired at different
magnification factors are simultaneously fed to networks during training for
learning multi-scale embeddings. In addition to the SMSE, to eliminate the
impact of class imbalance, instead of using the hard sample mining strategy
that intuitively discards some easy samples, we introduce a new reinforced
focal loss to simultaneously punish hard misclassified samples while
suppressing easy well-classified samples. Experimental results show that the
SMSE improves the performance for histopathological image classification tasks
for both breast and liver cancers by a large margin compared to previous
methods. In particular, the SMSE achieves the best performance on the BreakHis
benchmark with an improvement ranging from 5% to 18% compared to previous
methods using traditional features.