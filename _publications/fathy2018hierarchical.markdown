---
layout: publication
title: Hierarchical Metric Learning And Matching For 2D And 3D Geometric Correspondences
authors: Mohammed E. Fathy, Quoc-Huy Tran, M. Zeeshan Zia, Paul Vernaza, Manmohan
  Chandraker
conference: Lecture Notes in Computer Science
year: 2018
bibkey: fathy2018hierarchical
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.07231'}]
tags: ["Distance Metric Learning"]
short_authors: Fathy et al.
---
Interest point descriptors have fueled progress on almost every problem in
computer vision. Recent advances in deep neural networks have enabled
task-specific learned descriptors that outperform hand-crafted descriptors on
many problems. We demonstrate that commonly used metric learning approaches do
not optimally leverage the feature hierarchies learned in a Convolutional
Neural Network (CNN), especially when applied to the task of geometric feature
matching. While a metric loss applied to the deepest layer of a CNN, is often
expected to yield ideal features irrespective of the task, in fact the growing
receptive field as well as striding effects cause shallower features to be
better at high precision matching tasks. We leverage this insight together with
explicit supervision at multiple levels of the feature hierarchy for better
regularization, to learn more effective descriptors in the context of geometric
matching tasks. Further, we propose to use activation maps at different layers
of a CNN, as an effective and principled replacement for the multi-resolution
image pyramids often used for matching tasks. We propose concrete CNN
architectures employing these ideas, and evaluate them on multiple datasets for
2D and 3D geometric matching as well as optical flow, demonstrating
state-of-the-art results and generalization across datasets.