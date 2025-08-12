---
layout: publication
title: Incremental Few-shot Semantic Segmentation Via Embedding Adaptive-update And
  Hyper-class Representation
authors: Guangchen Shi, Yirui Wu, Jun Liu, Shaohua Wan, Wenhai Wang, Tong Lu
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: shi2022incremental
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.12964'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Shi et al.
---
Incremental few-shot semantic segmentation (IFSS) targets at incrementally
expanding model's capacity to segment new class of images supervised by only a
few samples. However, features learned on old classes could significantly
drift, causing catastrophic forgetting. Moreover, few samples for pixel-level
segmentation on new classes lead to notorious overfitting issues in each
learning session. In this paper, we explicitly represent class-based knowledge
for semantic segmentation as a category embedding and a hyper-class embedding,
where the former describes exclusive semantical properties, and the latter
expresses hyper-class knowledge as class-shared semantic properties. Aiming to
solve IFSS problems, we present EHNet, i.e., Embedding adaptive-update and
Hyper-class representation Network from two aspects. First, we propose an
embedding adaptive-update strategy to avoid feature drift, which maintains old
knowledge by hyper-class representation, and adaptively update category
embeddings with a class-attention scheme to involve new classes learned in
individual sessions. Second, to resist overfitting issues caused by few
training samples, a hyper-class embedding is learned by clustering all category
embeddings for initialization and aligned with category embedding of the new
class for enhancement, where learned knowledge assists to learn new knowledge,
thus alleviating performance dependence on training data scale. Significantly,
these two designs provide representation capability for classes with sufficient
semantics and limited biases, enabling to perform segmentation tasks requiring
high semantic dependence. Experiments on PASCAL-5i and COCO datasets show that
EHNet achieves new state-of-the-art performance with remarkable advantages.