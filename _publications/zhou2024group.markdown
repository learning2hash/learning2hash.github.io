---
layout: publication
title: 'Group-on: Boosting One-shot Segmentation With Supportive Query'
authors: Hanjing Zhou, Mingze Yin, Danny Chen, Jian Wu, Jintai Chen
conference: ICME 2025
year: 2024
bibkey: zhou2024group
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.11871'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhou et al.
---
One-shot semantic segmentation aims to segment query images given only ONE annotated support image of the same class. This task is challenging because target objects in the support and query images can be largely different in appearance and pose (i.e., intra-class variation). Prior works suggested that incorporating more annotated support images in few-shot settings boosts performances but increases costs due to additional manual labeling. In this paper, we propose a novel and effective approach for ONE-shot semantic segmentation, called Group-On, which packs multiple query images in batches for the benefit of mutual knowledge support within the same category. Specifically, after coarse segmentation masks of the batch of queries are predicted, query-mask pairs act as pseudo support data to enhance mask predictions mutually. To effectively steer such process, we construct an innovative MoME module, where a flexible number of mask experts are guided by a scene-driven router and work together to make comprehensive decisions, fully promoting mutual benefits of queries. Comprehensive experiments on three standard benchmarks show that, in the ONE-shot setting, Group-On significantly outperforms previous works by considerable margins. With only one annotated support image, Group-On can be even competitive with the counterparts using 5 annotated images.