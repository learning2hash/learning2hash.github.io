---
layout: publication
title: Label Self-adaption Hashing For Image Retrieval
authors: Lu Jianglin, Lai, Wang, Zhou
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: lu2025label
citations: 1
additional_links: [{name: Paper, url: 'https://ailb-web.ing.unimore.it/icpr/author/4323'}]
tags: ["Hashing-Methods", "Neural-Hashing", "Compact-Codes", "Efficiency", "Scalability", "Image-Retrieval", "Memory-Efficiency", "Tools-&-Libraries", "Supervised", "Evaluation", "Unsupervised"]
short_authors: Lu et al.
---
Hashing has attracted widespread attention in image retrieval because of its fast retrieval speed and low storage cost. Compared with supervised methods, unsupervised hashing methods are more reasonable and suitable for large-scale image retrieval since it is always difficult and expensive to collect true labels of the massive data. Without label information, however, unsupervised hashing methods can not guarantee the quality of learned binary codes. To resolve this dilemma, this paper proposes a novel unsupervised hashing method called Label Self-Adaption Hashing (LSAH), which contains effective hashing function learning part and self-adaption label generation part. In the first part, we utilize anchor graph to keep the local structure of the data and introduce joint sparsity into the model to extract effective features for high-quality binary code learning. In the second part, a self-adaptive cluster label matrix is learned from the data under the assumption that the nearest neighbor points should have a large probability to be in the same cluster. Therefore, the proposed LSAH can make full use of the potential discriminative information of the data to guide the learning of binary code. It is worth noting that LSAH can learn effective binary codes, hashing function and cluster labels simultaneously in a unified optimization framework. To solve the resulting optimization problem, an Augmented Lagrange Multiplier based iterative algorithm is elaborately designed. Extensive experiments on three large-scale data sets indicate the promising performance of the proposed LSAH.