---
layout: publication
title: Memory-guided Unsupervised Image-to-image Translation
authors: Somi Jeong, Youngjung Kim, Eungbean Lee, Kwanghoon Sohn
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: jeong2021memory
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.05170'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Jeong et al.
---
We present a novel unsupervised framework for instance-level image-to-image
translation. Although recent advances have been made by incorporating
additional object annotations, existing methods often fail to handle images
with multiple disparate objects. The main cause is that, during inference, they
apply a global style to the whole image and do not consider the large style
discrepancy between instance and background, or within instances. To address
this problem, we propose a class-aware memory network that explicitly reasons
about local style variations. A key-values memory structure, with a set of
read/update operations, is introduced to record class-wise style variations and
access them without requiring an object detector at the test time. The key
stores a domain-agnostic content representation for allocating memory items,
while the values encode domain-specific style representations. We also present
a feature contrastive loss to boost the discriminative power of memory items.
We show that by incorporating our memory, we can transfer class-aware and
accurate style representations across domains. Experimental results demonstrate
that our model outperforms recent instance-level methods and achieves
state-of-the-art performance.