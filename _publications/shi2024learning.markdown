---
layout: publication
title: Learning To Adapt Category Consistent Meta-feature Of CLIP For Few-shot Classification
authors: Jiaying Shi, Xuetong Xue, Shenghui Xu
conference: Arxiv
year: 2024
bibkey: shi2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.05647'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jiaying Shi, Xuetong Xue, Shenghui Xu
---
The recent CLIP-based methods have shown promising zero-shot and few-shot
performance on image classification tasks. Existing approaches such as CoOp and
Tip-Adapter only focus on high-level visual features that are fully aligned
with textual features representing the ``Summary" of the image. However, the
goal of few-shot learning is to classify unseen images of the same category
with few labeled samples. Especially, in contrast to high-level
representations, local representations (LRs) at low-level are more consistent
between seen and unseen samples. Based on this point, we propose the
Meta-Feature Adaption method (MF-Adapter) that combines the complementary
strengths of both LRs and high-level semantic representations. Specifically, we
introduce the Meta-Feature Unit (MF-Unit), which is a simple yet effective
local similarity metric to measure category-consistent local context in an
inductive manner. Then we train an MF-Adapter to map image features to MF-Unit
for adequately generalizing the intra-class knowledge between unseen images and
the support set. Extensive experiments show that our proposed method is
superior to the state-of-the-art CLIP downstream few-shot classification
methods, even showing stronger performance on a set of challenging visual
classification tasks.