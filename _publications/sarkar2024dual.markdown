---
layout: publication
title: 'Dual Pose-invariant Embeddings: Learning Category And Object-specific Discriminative
  Representations For Recognition And Retrieval'
authors: Rohan Sarkar, Avinash Kak
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: sarkar2024dual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.00272'}]
tags: ["CVPR", "Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Rohan Sarkar, Avinash Kak
---
In the context of pose-invariant object recognition and retrieval, we
demonstrate that it is possible to achieve significant improvements in
performance if both the category-based and the object-identity-based embeddings
are learned simultaneously during training. In hindsight, that sounds intuitive
because learning about the categories is more fundamental than learning about
the individual objects that correspond to those categories. However, to the
best of what we know, no prior work in pose-invariant learning has demonstrated
this effect. This paper presents an attention-based dual-encoder architecture
with specially designed loss functions that optimize the inter- and intra-class
distances simultaneously in two different embedding spaces, one for the
category embeddings and the other for the object-level embeddings. The loss
functions we have proposed are pose-invariant ranking losses that are designed
to minimize the intra-class distances and maximize the inter-class distances in
the dual representation spaces. We demonstrate the power of our approach with
three challenging multi-view datasets, ModelNet-40, ObjectPI, and FG3D. With
our dual approach, for single-view object recognition, we outperform the
previous best by 20.0% on ModelNet40, 2.0% on ObjectPI, and 46.5% on FG3D. On
the other hand, for single-view object retrieval, we outperform the previous
best by 33.7% on ModelNet40, 18.8% on ObjectPI, and 56.9% on FG3D.