---
layout: publication
title: A Unified Weighting Framework For Evaluating Nearest Neighbour Classification
authors: Oliver Urs Lenz, Henri Bollaert, Chris Cornelis
conference: Arxiv
year: 2023
bibkey: lenz2023unified
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.16872'}]
tags: ["Evaluation"]
short_authors: Oliver Urs Lenz, Henri Bollaert, Chris Cornelis
---
We present the first comprehensive and large-scale evaluation of classical (NN), fuzzy (FNN) and fuzzy rough (FRNN) nearest neighbour classification. We standardise existing proposals for nearest neighbour weighting with kernel functions, applied to the distance values and/or ranks of the nearest neighbours of a test instance. In particular, we show that the theoretically optimal Samworth weights converge to a kernel. Kernel functions are closely related to fuzzy negation operators, and we propose a new kernel based on Yager negation. We also consider various distance and scaling measures, which we show can be related to each other. Through a systematic series of experiments on 85 real-life classification datasets, we find that NN, FNN and FRNN all perform best with Boscovich distance, and that NN and FRNN perform best with a combination of Samworth rank- and distance-weights and scaling by the mean absolute deviation around the median (\(r_1\)), the standard deviation (\(r_2\)) or the semi-interquartile range (\(r_\{\infty\}^*\)), while FNN performs best with only Samworth distance-weights and \(r_1\)- or \(r_2\)-scaling. However, NN achieves comparable performance with Yager-\(\frac\{1\}\{2\}\) distance-weights, which are simpler to implement than a combination of Samworth distance- and rank-weights. Finally, FRNN generally outperforms NN, which in turn performs systematically better than FNN.