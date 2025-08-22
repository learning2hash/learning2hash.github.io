---
layout: publication
title: Deep Feature Learning With Relative Distance Comparison For Person Re-identification
authors: Shengyong Ding, Liang Lin, Guangrun Wang, Hongyang Chao
conference: Pattern Recognition
year: 2015
bibkey: ding2015deep
citations: 730
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.03622'}]
tags: ["CVPR", "Distance Metric Learning", "Evaluation", "Tools & Libraries"]
short_authors: Ding et al.
---
Identifying the same individual across different scenes is an important yet
difficult task in intelligent video surveillance. Its main difficulty lies in
how to preserve similarity of the same person against large appearance and
structure variation while discriminating different individuals. In this paper,
we present a scalable distance driven feature learning framework based on the
deep neural network for person re-identification, and demonstrate its
effectiveness to handle the existing challenges. Specifically, given the
training images with the class labels (person IDs), we first produce a large
number of triplet units, each of which contains three images, i.e. one person
with a matched reference and a mismatched reference. Treating the units as the
input, we build the convolutional neural network to generate the layered
representations, and follow with the \(L2\) distance metric. By means of
parameter optimization, our framework tends to maximize the relative distance
between the matched pair and the mismatched pair for each triplet unit.
Moreover, a nontrivial issue arising with the framework is that the triplet
organization cubically enlarges the number of training triplets, as one image
can be involved into several triplet units. To overcome this problem, we
develop an effective triplet generation scheme and an optimized gradient
descent algorithm, making the computational load mainly depends on the number
of original images instead of the number of triplets. On several challenging
databases, our approach achieves very promising results and outperforms other
state-of-the-art approaches.