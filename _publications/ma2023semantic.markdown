---
layout: publication
title: Semantic-aware Dual Contrastive Learning For Multi-label Image Classification
authors: Leilei Ma, Dengdi Sun, Lei Wang, Haifeng Zhao, Bin Luo
conference: Frontiers in Artificial Intelligence and Applications
year: 2023
bibkey: ma2023semantic
citations: 3
additional_links: [{name: Code, url: 'https://github.com/yu-gi-oh-leilei/SADCL'},
  {name: Paper, url: 'https://arxiv.org/abs/2307.09715'}]
tags: ["Self-Supervised"]
short_authors: Ma et al.
---
Extracting image semantics effectively and assigning corresponding labels to
multiple objects or attributes for natural images is challenging due to the
complex scene contents and confusing label dependencies. Recent works have
focused on modeling label relationships with graph and understanding object
regions using class activation maps (CAM). However, these methods ignore the
complex intra- and inter-category relationships among specific semantic
features, and CAM is prone to generate noisy information. To this end, we
propose a novel semantic-aware dual contrastive learning framework that
incorporates sample-to-sample contrastive learning (SSCL) as well as
prototype-to-sample contrastive learning (PSCL). Specifically, we leverage
semantic-aware representation learning to extract category-related local
discriminative features and construct category prototypes. Then based on SSCL,
label-level visual representations of the same category are aggregated
together, and features belonging to distinct categories are separated.
Meanwhile, we construct a novel PSCL module to narrow the distance between
positive samples and category prototypes and push negative samples away from
the corresponding category prototypes. Finally, the discriminative label-level
features related to the image content are accurately captured by the joint
training of the above three parts. Experiments on five challenging large-scale
public datasets demonstrate that our proposed method is effective and
outperforms the state-of-the-art methods. Code and supplementary materials are
released on https://github.com/yu-gi-oh-leilei/SADCL.