---
layout: publication
title: Steerable Equivariant Representation Learning
authors: Sangnie Bhardwaj, Willie McClinton, Tongzhou Wang, Guillaume Lajoie, Chen
  Sun, Phillip Isola, Dilip Krishnan
conference: Arxiv
year: 2023
bibkey: bhardwaj2023steerable
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.11349'}]
tags: ["Evaluation", "Image Retrieval", "Robustness", "Self-Supervised", "Supervised"]
short_authors: Bhardwaj et al.
---
Pre-trained deep image representations are useful for post-training tasks
such as classification through transfer learning, image retrieval, and object
detection. Data augmentations are a crucial aspect of pre-training robust
representations in both supervised and self-supervised settings. Data
augmentations explicitly or implicitly promote invariance in the embedding
space to the input image transformations. This invariance reduces
generalization to those downstream tasks which rely on sensitivity to these
particular data augmentations. In this paper, we propose a method of learning
representations that are instead equivariant to data augmentations. We achieve
this equivariance through the use of steerable representations. Our
representations can be manipulated directly in embedding space via learned
linear maps. We demonstrate that our resulting steerable and equivariant
representations lead to better performance on transfer learning and robustness:
e.g. we improve linear probe top-1 accuracy by between 1% to 3% for transfer;
and ImageNet-C accuracy by upto 3.4%. We further show that the steerability of
our representations provides significant speedup (nearly 50x) for test-time
augmentations; by applying a large number of augmentations for
out-of-distribution detection, we significantly improve OOD AUC on the
ImageNet-C dataset over an invariant representation.