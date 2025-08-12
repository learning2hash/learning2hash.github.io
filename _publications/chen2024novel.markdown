---
layout: publication
title: A Novel Pseudo Nearest Neighbor Classification Method Using Local Harmonic
  Mean Distance
authors: Junzhuo Chen, Zhixin Lu, Shitong Kang
conference: Arxiv
year: 2024
bibkey: chen2024novel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.06238'}]
tags: ["Distance Metric Learning"]
short_authors: Junzhuo Chen, Zhixin Lu, Shitong Kang
---
In the realm of machine learning, the KNN classification algorithm is widely
recognized for its simplicity and efficiency. However, its sensitivity to the K
value poses challenges, especially with small sample sizes or outliers,
impacting classification performance. This article introduces a novel KNN-based
classifier called LMPHNN (Novel Pseudo Nearest Neighbor Classification Method
Using Local Harmonic Mean Distance). LMPHNN leverages harmonic mean distance
(HMD) to improve classification performance based on LMPNN rules and HMD. The
classifier begins by identifying k nearest neighbors for each class and
generates distinct local vectors as prototypes. Pseudo nearest neighbors (PNNs)
are then created based on the local mean for each class, determined by
comparing the HMD of the sample with the initial k group. Classification is
determined by calculating the Euclidean distance between the query sample and
PNNs, based on the local mean of these categories. Extensive experiments on
various real UCI datasets and combined datasets compare LMPHNN with seven
KNN-based classifiers, using precision, recall, accuracy, and F1 as evaluation
metrics. LMPHNN achieves an average precision of 97%, surpassing other methods
by 14%. The average recall improves by 12%, with an average accuracy
enhancement of 5%. Additionally, LMPHNN demonstrates a 13% higher average F1
value compared to other methods. In summary, LMPHNN outperforms other
classifiers, showcasing lower sensitivity with small sample sizes.