---
layout: publication
title: 'RECLIP: Resource-efficient CLIP By Training With Small Images'
authors: Runze Li, Dahun Kim, Bir Bhanu, Weicheng Kuo
conference: Arxiv
year: 2023
bibkey: li2023reclip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.06028'}]
tags: ["Efficiency", "Few Shot & Zero Shot", "Scalability", "Self-Supervised"]
short_authors: Li et al.
---
We present RECLIP (Resource-efficient CLIP), a simple method that minimizes
computational resource footprint for CLIP (Contrastive Language Image
Pretraining). Inspired by the notion of coarse-to-fine in computer vision, we
leverage small images to learn from large-scale language supervision
efficiently, and finetune the model with high-resolution data in the end. Since
the complexity of the vision transformer heavily depends on input image size,
our approach significantly reduces the training resource requirements both in
theory and in practice. Using the same batch size and training epoch, RECLIP
achieves highly competitive zero-shot classification and image-text retrieval
accuracy with 6 to 8x less computational resources and 7 to 9x fewer FLOPs than
the baseline. Compared to the state-of-the-art contrastive learning methods,
RECLIP demonstrates 5 to 59x training resource savings while maintaining highly
competitive zero-shot classification and retrieval performance. Finally, RECLIP
matches the state of the art in transfer learning to open-vocabulary detection
tasks, achieving 32 APr on LVIS. We hope this work will pave the path for the
broader research community to explore language supervised pretraining in
resource-friendly settings.