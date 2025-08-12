---
layout: publication
title: 'Patternnet: Visual Pattern Mining With Deep Neural Network'
authors: Hongzhi Li, Joseph G. Ellis, Lei Zhang, Shih-Fu Chang
conference: Arxiv
year: 2017
bibkey: li2017patternnet
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.06339'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Li et al.
---
Visual patterns represent the discernible regularity in the visual world.
They capture the essential nature of visual objects or scenes. Understanding
and modeling visual patterns is a fundamental problem in visual recognition
that has wide ranging applications. In this paper, we study the problem of
visual pattern mining and propose a novel deep neural network architecture
called PatternNet for discovering these patterns that are both discriminative
and representative. The proposed PatternNet leverages the filters in the last
convolution layer of a convolutional neural network to find locally consistent
visual patches, and by combining these filters we can effectively discover
unique visual patterns. In addition, PatternNet can discover visual patterns
efficiently without performing expensive image patch sampling, and this
advantage provides an order of magnitude speedup compared to most other
approaches. We evaluate the proposed PatternNet subjectively by showing
randomly selected visual patterns which are discovered by our method and
quantitatively by performing image classification with the identified visual
patterns and comparing our performance with the current state-of-the-art. We
also directly evaluate the quality of the discovered visual patterns by
leveraging the identified patterns as proposed objects in an image and compare
with other relevant methods. Our proposed network and procedure, PatterNet, is
able to outperform competing methods for the tasks described.