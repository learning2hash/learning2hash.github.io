---
layout: publication
title: On The Resistance Of Nearest Neighbor To Random Noisy Labels
authors: Wei Gao, Bin-Bin Yang, Zhi-Hua Zhou
conference: Arxiv
year: 2016
bibkey: gao2016resistance
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.07526'}]
tags: ["Robustness"]
short_authors: Wei Gao, Bin-Bin Yang, Zhi-Hua Zhou
---
Nearest neighbor has always been one of the most appealing non-parametric
approaches in machine learning, pattern recognition, computer vision, etc.
Previous empirical studies partly shows that nearest neighbor is resistant to
noise, yet there is a lack of deep analysis. This work presents the
finite-sample and distribution-dependent bounds on the consistency of nearest
neighbor in the random noise setting. The theoretical results show that, for
asymmetric noises, k-nearest neighbor is robust enough to classify most data
correctly, except for a handful of examples, whose labels are totally misled by
random noises. For symmetric noises, however, k-nearest neighbor achieves the
same consistent rate as that of noise-free setting, which verifies the
resistance of k-nearest neighbor to random noisy labels. Motivated by the
theoretical analysis, we propose the Robust k-Nearest Neighbor (RkNN) approach
to deal with noisy labels. The basic idea is to make unilateral corrections to
examples, whose labels are totally misled by random noises, and classify the
others directly by utilizing the robustness of k-nearest neighbor. We verify
the effectiveness of the proposed algorithm both theoretically and empirically.