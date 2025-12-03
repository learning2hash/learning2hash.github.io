---
layout: publication
title: How To Handle Sketch-abstraction In Sketch-based Image Retrieval?
authors: Subhadeep Koley, Ayan Kumar Bhunia, Aneeshan Sain, Pinaki Nath Chowdhury,
  Tao Xiang, Yi-Zhe Song
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: koley2024how
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07203'}]
tags: ["CVPR", "Distance Metric Learning", "Evaluation", "Image Retrieval", "Tools & Libraries"]
short_authors: Koley et al.
---
In this paper, we propose a novel abstraction-aware sketch-based image
retrieval framework capable of handling sketch abstraction at varied levels.
Prior works had mainly focused on tackling sub-factors such as drawing style
and order, we instead attempt to model abstraction as a whole, and propose
feature-level and retrieval granularity-level designs so that the system builds
into its DNA the necessary means to interpret abstraction. On learning
abstraction-aware features, we for the first-time harness the rich semantic
embedding of pre-trained StyleGAN model, together with a novel
abstraction-level mapper that deciphers the level of abstraction and
dynamically selects appropriate dimensions in the feature matrix
correspondingly, to construct a feature matrix embedding that can be freely
traversed to accommodate different levels of abstraction. For granularity-level
abstraction understanding, we dictate that the retrieval model should not treat
all abstraction-levels equally and introduce a differentiable surrogate Acc.@q
loss to inject that understanding into the system. Different to the
gold-standard triplet loss, our Acc.@q loss uniquely allows a sketch to
narrow/broaden its focus in terms of how stringent the evaluation should be -
the more abstract a sketch, the less stringent (higher q). Extensive
experiments depict our method to outperform existing state-of-the-arts in
standard SBIR tasks along with challenging scenarios like early retrieval,
forensic sketch-photo matching, and style-invariant retrieval.