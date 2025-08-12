---
layout: publication
title: Unsupervised Feature Learning With Emergent Data-driven Prototypicality
authors: Yunhui Guo, Youren Zhang, Yubei Chen, Stella X. Yu
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: guo2023unsupervised
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.01421'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Guo et al.
---
Given an image set without any labels, our goal is to train a model that maps
each image to a point in a feature space such that, not only proximity
indicates visual similarity, but where it is located directly encodes how
prototypical the image is according to the dataset.
  Our key insight is to perform unsupervised feature learning in hyperbolic
instead of Euclidean space, where the distance between points still reflect
image similarity, and yet we gain additional capacity for representing
prototypicality with the location of the point: The closer it is to the origin,
the more prototypical it is. The latter property is simply emergent from
optimizing the usual metric learning objective: The image similar to many
training instances is best placed at the center of corresponding points in
Euclidean space, but closer to the origin in hyperbolic space.
  We propose an unsupervised feature learning algorithm in Hyperbolic space
with sphere pACKing. HACK first generates uniformly packed particles in the
Poincar\'e ball of hyperbolic space and then assigns each image uniquely to
each particle. Images after congealing are regarded more typical of the dataset
it belongs to. With our feature mapper simply trained to spread out training
instances in hyperbolic space, we observe that images move closer to the origin
with congealing, validating our idea of unsupervised prototypicality discovery.
We demonstrate that our data-driven prototypicality provides an easy and
superior unsupervised instance selection to reduce sample complexity, increase
model generalization with atypical instances and robustness with typical ones.