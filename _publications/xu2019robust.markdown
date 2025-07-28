---
layout: publication
title: Robust Angular Local Descriptor Learning
authors: Yanwu Xu, Mingming Gong, Tongliang Liu, Kayhan Batmanghelich, Chaohui Wang
conference: Lecture Notes in Computer Science
year: 2019
bibkey: xu2019robust
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.07076'}]
tags: ["Distance Metric Learning", "Robustness"]
short_authors: Xu et al.
---
In recent years, the learned local descriptors have outperformed handcrafted
ones by a large margin, due to the powerful deep convolutional neural network
architectures such as L2-Net [1] and triplet based metric learning [2].
However, there are two problems in the current methods, which hinders the
overall performance. Firstly, the widely-used margin loss is sensitive to
incorrect correspondences, which are prevalent in the existing local descriptor
learning datasets. Second, the L2 distance ignores the fact that the feature
vectors have been normalized to unit norm. To tackle these two problems and
further boost the performance, we propose a robust angular loss which 1) uses
cosine similarity instead of L2 distance to compare descriptors and 2) relies
on a robust loss function that gives smaller penalty to triplets with negative
relative similarity. The resulting descriptor shows robustness on different
datasets, reaching the state-of-the-art result on Brown dataset , as well as
demonstrating excellent generalization ability on the Hpatches dataset and a
Wide Baseline Stereo dataset.