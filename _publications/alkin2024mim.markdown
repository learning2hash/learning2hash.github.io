---
layout: publication
title: 'Mim-refiner: A Contrastive Learning Boost From Intermediate Pre-trained Representations'
authors: Benedikt Alkin, Lukas Miklautz, Sepp Hochreiter, Johannes Brandstetter
conference: Arxiv
year: 2024
bibkey: alkin2024mim
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.10093'}]
tags: ["Evaluation", "Self-Supervised"]
short_authors: Alkin et al.
---
We introduce MIM (Masked Image Modeling)-Refiner, a contrastive learning
boost for pre-trained MIM models. MIM-Refiner is motivated by the insight that
strong representations within MIM models generally reside in intermediate
layers. Accordingly, MIM-Refiner leverages multiple contrastive heads that are
connected to different intermediate layers. In each head, a modified nearest
neighbor objective constructs semantic clusters that capture semantic
information which improves performance on downstream tasks, including
off-the-shelf and fine-tuning settings.
  The refinement process is short and simple - yet highly effective. Within a
few epochs, we refine the features of MIM models from subpar to
state-of-the-art, off-the-shelf features. Refining a ViT-H, pre-trained with
data2vec 2.0 on ImageNet-1K, sets a new state-of-the-art in linear probing
(84.7%) and low-shot classification among models that are pre-trained on
ImageNet-1K. MIM-Refiner efficiently combines the advantages of MIM and ID
objectives and compares favorably against previous state-of-the-art SSL models
on a variety of benchmarks such as low-shot classification, long-tailed
classification, clustering and semantic segmentation.