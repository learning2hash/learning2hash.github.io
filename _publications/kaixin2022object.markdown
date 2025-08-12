---
layout: publication
title: Object-aware Self-supervised Multi-label Learning
authors: Xu Kaixin, Liu Liyang, Zhao Ziyuan, Zeng Zeng, Bharadwaj Veeravalli
conference: 2022 IEEE International Conference on Image Processing (ICIP)
year: 2022
bibkey: kaixin2022object
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.07028'}]
tags: ["Self-Supervised"]
short_authors: Kaixin et al.
---
Multi-label Learning on Image data has been widely exploited with deep
learning models. However, supervised training on deep CNN models often cannot
discover sufficient discriminative features for classification. As a result,
numerous self-supervision methods are proposed to learn more robust image
representations. However, most self-supervised approaches focus on
single-instance single-label data and fall short on more complex images with
multiple objects. Therefore, we propose an Object-Aware Self-Supervision (OASS)
method to obtain more fine-grained representations for multi-label learning,
dynamically generating auxiliary tasks based on object locations. Secondly, the
robust representation learned by OASS can be leveraged to efficiently generate
Class-Specific Instances (CSI) in a proposal-free fashion to better guide
multi-label supervision signal transfer to instances. Extensive experiments on
the VOC2012 dataset for multi-label classification demonstrate the
effectiveness of the proposed method against the state-of-the-art counterparts.