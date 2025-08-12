---
layout: publication
title: 'Hubs And Hyperspheres: Reducing Hubness And Improving Transductive Few-shot
  Learning With Hyperspherical Embeddings'
authors: "Daniel J. Trosten, Rwiddhi Chakraborty, Sigurd L\xF8kse, Kristoffer Knutsen\
  \ Wickstr\xF8m, Robert Jenssen, Michael C. Kampffmeyer"
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: trosten2023hubs
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09352'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Trosten et al.
---
Distance-based classification is frequently used in transductive few-shot
learning (FSL). However, due to the high-dimensionality of image
representations, FSL classifiers are prone to suffer from the hubness problem,
where a few points (hubs) occur frequently in multiple nearest neighbour lists
of other points. Hubness negatively impacts distance-based classification when
hubs from one class appear often among the nearest neighbors of points from
another class, degrading the classifier's performance. To address the hubness
problem in FSL, we first prove that hubness can be eliminated by distributing
representations uniformly on the hypersphere. We then propose two new
approaches to embed representations on the hypersphere, which we prove optimize
a tradeoff between uniformity and local similarity preservation -- reducing
hubness while retaining class structure. Our experiments show that the proposed
methods reduce hubness, and significantly improves transductive FSL accuracy
for a wide range of classifiers.