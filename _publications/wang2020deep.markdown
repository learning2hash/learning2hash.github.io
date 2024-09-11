---
layout: publication
title: "Deep Hashing with Active Pairwise Supervision"
authors: Ziwei Wang, Quan Zheng, Jiwen Lu, and Jie Zhou
conference: ECCV
year: 2020
bibkey: wang2020deep
additional_links:
   - {name: "PDF", url: "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123640511.pdf"}
tags: ["ECCV", "Deep Learning", "Supervised"]
---
In this paper, we propose a Deep Hashing method with Active Pairwise Supervision(DH-APS). Conventional methods with passive
pairwise supervision obtain labeled data for training and require large
amount of annotations to reach their full potential, which are not feasible in realistic retrieval tasks. On the contrary, we actively select a small
quantity of informative samples for annotation to provide effective pairwise supervision so that discriminative hash codes can be obtained with
limited annotation budget. Specifically, we generalize the structural risk
minimization principle and obtain three criteria for the pairwise supervision acquisition: uncertainty, representativeness and diversity. Accordingly, samples involved in the following training pairs should be labeled:
pairs with most uncertain similarity, pairs that minimize the discrepancy
between labeled and unlabeled data, and pairs which are most different
from the annotated data, so that the discriminality and generalization ability of the learned hash codes are significantly strengthened. Moreover,
our DH-APS can also be employed as a plug-and-play module for semisupervised hashing methods to further enhance the performance. Experiments demonstrate that the presented DH-APS achieves the accuracy
of supervised hashing methods with only 30% labeled training samples
and improves the semi-supervised binary codes by a sizable margin.
