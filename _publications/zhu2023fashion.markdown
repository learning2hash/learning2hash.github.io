---
layout: publication
title: Fashion Image Retrieval With Multi-granular Alignment
authors: Jinkuan Zhu, Hao Huang, Qiao Deng, Xiyao Li
conference: Arxiv
year: 2023
bibkey: zhu2023fashion
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.08902'}]
tags: [Datasets, Image Retrieval]
short_authors: Zhu et al.
---
Fashion image retrieval task aims to search relevant clothing items of a
query image from the gallery. The previous recipes focus on designing different
distance-based loss functions, pulling relevant pairs to be close and pushing
irrelevant images apart. However, these methods ignore fine-grained features
(e.g. neckband, cuff) of clothing images. In this paper, we propose a novel
fashion image retrieval method leveraging both global and fine-grained
features, dubbed Multi-Granular Alignment (MGA). Specifically, we design a
Fine-Granular Aggregator(FGA) to capture and aggregate detailed patterns. Then
we propose Attention-based Token Alignment (ATA) to align image features at the
multi-granular level in a coarse-to-fine manner. To prove the effectiveness of
our proposed method, we conduct experiments on two sub-tasks (In-Shop &
Consumer2Shop) of the public fashion datasets DeepFashion. The experimental
results show that our MGA outperforms the state-of-the-art methods by 1.8% and
0.6% in the two sub-tasks on the R@1 metric, respectively.