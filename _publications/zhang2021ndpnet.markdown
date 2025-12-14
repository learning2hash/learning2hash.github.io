---
layout: publication
title: 'Ndpnet: A Novel Non-linear Data Projection Network For Few-shot Fine-grained
  Image Classification'
authors: Weichuan Zhang, Xuefang Liu, Zhe Xue, Yongsheng Gao, Changming Sun
conference: Arxiv
year: 2021
bibkey: zhang2021ndpnet
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06988'}]
tags: [Evaluation, Distance Metric Learning, Few-shot & Zero-shot]
short_authors: Zhang et al.
---
Metric-based few-shot fine-grained image classification (FSFGIC) aims to
learn a transferable feature embedding network by estimating the similarities
between query images and support classes from very few examples. In this work,
we propose, for the first time, to introduce the non-linear data projection
concept into the design of FSFGIC architecture in order to address the limited
sample problem in few-shot learning and at the same time to increase the
discriminability of the model for fine-grained image classification.
Specifically, we first design a feature re-abstraction embedding network that
has the ability to not only obtain the required semantic features for effective
metric learning but also re-enhance such features with finer details from input
images. Then the descriptors of the query images and the support classes are
projected into different non-linear spaces in our proposed similarity metric
learning network to learn discriminative projection factors. This design can
effectively operate in the challenging and restricted condition of a FSFGIC
task for making the distance between the samples within the same class smaller
and the distance between samples from different classes larger and for reducing
the coupling relationship between samples from different categories.
Furthermore, a novel similarity measure based on the proposed non-linear data
project is presented for evaluating the relationships of feature information
between a query image and a support set. It is worth to note that our proposed
architecture can be easily embedded into any episodic training mechanisms for
end-to-end training from scratch. Extensive experiments on FSFGIC tasks
demonstrate the superiority of the proposed methods over the state-of-the-art
benchmarks.