---
layout: publication
title: Local Descriptors Weighted Adaptive Threshold Filtering For Few-shot Learning
authors: Bingchen Yan
conference: Arxiv
year: 2024
bibkey: yan2024local
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.15924'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bingchen Yan
---
Few-shot image classification is a challenging task in the field of machine
learning, involving the identification of new categories using a limited number
of labeled samples. In recent years, methods based on local descriptors have
made significant progress in this area. However, the key to improving
classification accuracy lies in effectively filtering background noise and
accurately selecting critical local descriptors highly relevant to image
category information.
  To address this challenge, we propose an innovative weighted adaptive
threshold filtering (WATF) strategy for local descriptors. This strategy can
dynamically adjust based on the current task and image context, thereby
selecting local descriptors most relevant to the image category. This enables
the model to better focus on category-related information while effectively
mitigating interference from irrelevant background regions.
  To evaluate the effectiveness of our method, we adopted the N-way K-shot
experimental framework. Experimental results show that our method not only
improves the clustering effect of selected local descriptors but also
significantly enhances the discriminative ability between image categories.
Notably, our method maintains a simple and lightweight design philosophy
without introducing additional learnable parameters. This feature ensures
consistency in filtering capability during both training and testing phases,
further enhancing the reliability and practicality of the method.