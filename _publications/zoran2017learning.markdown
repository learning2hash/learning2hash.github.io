---
layout: publication
title: Learning Deep Nearest Neighbor Representations Using Differentiable Boundary
  Trees
authors: Daniel Zoran, Balaji Lakshminarayanan, Charles Blundell
conference: Arxiv
year: 2017
bibkey: zoran2017learning
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.08833'}]
tags: ["Efficiency"]
short_authors: Daniel Zoran, Balaji Lakshminarayanan, Charles Blundell
---
Nearest neighbor (kNN) methods have been gaining popularity in recent years
in light of advances in hardware and efficiency of algorithms. There is a
plethora of methods to choose from today, each with their own advantages and
disadvantages. One requirement shared between all kNN based methods is the need
for a good representation and distance measure between samples.
  We introduce a new method called differentiable boundary tree which allows
for learning deep kNN representations. We build on the recently proposed
boundary tree algorithm which allows for efficient nearest neighbor
classification, regression and retrieval. By modelling traversals in the tree
as stochastic events, we are able to form a differentiable cost function which
is associated with the tree's predictions. Using a deep neural network to
transform the data and back-propagating through the tree allows us to learn
good representations for kNN methods.
  We demonstrate that our method is able to learn suitable representations
allowing for very efficient trees with a clearly interpretable structure.