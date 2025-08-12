---
layout: publication
title: Improving The Hardnet Descriptor
authors: Milan Pultar
conference: Arxiv
year: 2020
bibkey: pultar2020improving
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.09699'}]
tags: []
short_authors: Milan Pultar
---
In the thesis we consider the problem of local feature descriptor learning
for wide baseline stereo focusing on the HardNet descriptor, which is close to
state-of-the-art. AMOS Patches dataset is introduced, which improves robustness
to illumination and appearance changes. It is based on registered images from
selected cameras from the AMOS dataset. We provide recommendations on the patch
dataset creation process and evaluate HardNet trained on data of different
modalities. We also introduce a dataset combination and reduction methods, that
allow comparable performance on a significantly smaller dataset.
  HardNet8, consistently outperforming the original HardNet, benefits from the
architectural choices made: connectivity pattern, final pooling, receptive
field, CNN building blocks found by manual or automatic search algorithms --
DARTS. We show impact of overlooked hyperparameters such as batch size and
length of training on the descriptor quality. PCA dimensionality reduction
further boosts performance and also reduces memory footprint.
  Finally, the insights gained lead to two HardNet8 descriptors: one performing
well on a variety of benchmarks -- HPatches, AMOS Patches and IMW Phototourism,
the other is optimized for IMW Phototourism.