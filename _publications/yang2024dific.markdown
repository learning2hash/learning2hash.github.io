---
layout: publication
title: 'Dific: Your Diffusion Model Holds The Secret To Fine-grained Clustering'
authors: Ruohong Yang, Peng Hu, Xi Peng, Xiting Liu, Yunfan Li
conference: Arxiv
year: 2024
bibkey: yang2024dific
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.18838'}]
tags: []
short_authors: Yang et al.
---
Fine-grained clustering is a practical yet challenging task, whose essence
lies in capturing the subtle differences between instances of different
classes. Such subtle differences can be easily disrupted by data augmentation
or be overwhelmed by redundant information in data, leading to significant
performance degradation for existing clustering methods. In this work, we
introduce DiFiC a fine-grained clustering method building upon the conditional
diffusion model. Distinct from existing works that focus on extracting
discriminative features from images, DiFiC resorts to deducing the textual
conditions used for image generation. To distill more precise and
clustering-favorable object semantics, DiFiC further regularizes the diffusion
target and guides the distillation process utilizing neighborhood similarity.
Extensive experiments demonstrate that DiFiC outperforms both state-of-the-art
discriminative and generative clustering methods on four fine-grained image
clustering benchmarks. We hope the success of DiFiC will inspire future
research to unlock the potential of diffusion models in tasks beyond
generation. The code will be released.