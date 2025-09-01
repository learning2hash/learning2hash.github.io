---
layout: publication
title: Improving Memory Banks For Unsupervised Learning With Large Mini-batch, Consistency
  And Hard Negative Mining
authors: "Adrian Bulat, Enrique S\xE1nchez-Lozano, Georgios Tzimiropoulos"
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: bulat2021improving
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04442'}]
tags: ["Datasets", "Distance Metric Learning", "ICASSP", "Unsupervised"]
short_authors: "Adrian Bulat, Enrique S\xE1nchez-Lozano, Georgios Tzimiropoulos"
---
An important component of unsupervised learning by instance-based
discrimination is a memory bank for storing a feature representation for each
training sample in the dataset. In this paper, we introduce 3 improvements to
the vanilla memory bank-based formulation which brings massive accuracy gains:
(a) Large mini-batch: we pull multiple augmentations for each sample within the
same batch and show that this leads to better models and enhanced memory bank
updates. (b) Consistency: we enforce the logits obtained by different
augmentations of the same sample to be close without trying to enforce
discrimination with respect to negative samples as proposed by previous
approaches. (c) Hard negative mining: since instance discrimination is not
meaningful for samples that are too visually similar, we devise a novel nearest
neighbour approach for improving the memory bank that gradually merges
extremely similar data samples that were previously forced to be apart by the
instance level classification loss. Overall, our approach greatly improves the
vanilla memory-bank based instance discrimination and outperforms all existing
methods for both seen and unseen testing categories with cosine similarity.