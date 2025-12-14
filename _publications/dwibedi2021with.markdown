---
layout: publication
title: 'With A Little Help From My Friends: Nearest-neighbor Contrastive Learning
  Of Visual Representations'
authors: Debidatta Dwibedi, Yusuf Aytar, Jonathan Tompson, Pierre Sermanet, Andrew
  Zisserman
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: dwibedi2021with
citations: 351
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14548'}]
tags: [Evaluation, Supervised, ICCV, Self-Supervised, Distance Metric Learning, Datasets]
short_authors: Dwibedi et al.
---
Self-supervised learning algorithms based on instance discrimination train
encoders to be invariant to pre-defined transformations of the same instance.
While most methods treat different views of the same image as positives for a
contrastive loss, we are interested in using positives from other instances in
the dataset. Our method, Nearest-Neighbor Contrastive Learning of visual
Representations (NNCLR), samples the nearest neighbors from the dataset in the
latent space, and treats them as positives. This provides more semantic
variations than pre-defined transformations.
  We find that using the nearest-neighbor as positive in contrastive losses
improves performance significantly on ImageNet classification, from 71.7% to
75.6%, outperforming previous state-of-the-art methods. On semi-supervised
learning benchmarks we improve performance significantly when only 1% ImageNet
labels are available, from 53.8% to 56.5%. On transfer learning benchmarks our
method outperforms state-of-the-art methods (including supervised learning with
ImageNet) on 8 out of 12 downstream datasets. Furthermore, we demonstrate
empirically that our method is less reliant on complex data augmentations. We
see a relative reduction of only 2.1% ImageNet Top-1 accuracy when we train
using only random crops.