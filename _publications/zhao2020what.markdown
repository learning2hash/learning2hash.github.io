---
layout: publication
title: What Makes Instance Discrimination Good For Transfer Learning?
authors: Nanxuan Zhao, Zhirong Wu, Rynson W. H. Lau, Stephen Lin
conference: Arxiv
year: 2020
bibkey: zhao2020what
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.06606'}]
tags: []
short_authors: Zhao et al.
---
Contrastive visual pretraining based on the instance discrimination pretext
task has made significant progress. Notably, recent work on unsupervised
pretraining has shown to surpass the supervised counterpart for finetuning
downstream applications such as object detection and segmentation. It comes as
a surprise that image annotations would be better left unused for transfer
learning. In this work, we investigate the following problems: What makes
instance discrimination pretraining good for transfer learning? What knowledge
is actually learned and transferred from these models? From this understanding
of instance discrimination, how can we better exploit human annotation labels
for pretraining? Our findings are threefold. First, what truly matters for the
transfer is low-level and mid-level representations, not high-level
representations. Second, the intra-category invariance enforced by the
traditional supervised model weakens transferability by increasing task
misalignment. Finally, supervised pretraining can be strengthened by following
an exemplar-based approach without explicit constraints among the instances
within the same category.