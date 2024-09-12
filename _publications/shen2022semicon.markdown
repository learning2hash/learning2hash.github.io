---
layout: publication
title: SEMICON A Learning-to-hash Solution for Large-scale Fine-grained Image Retrieval
authors: Shen Yang, Sun Xuhao, Wei Xiu-Shen, Jiang Qing-Yuan, Yang Jian
conference: "Arxiv"
year: 2022
bibkey: shen2022semicon
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2209.13833"}
tags: ['ARXIV', 'Image Retrieval', 'Independent', 'TIP']
---
In this paper we propose Suppression-Enhancing Mask based attention and Interactive Channel transformatiON (SEMICON) to learn binary hash codes for dealing with large-scale fine-grained image retrieval tasks. In SEMICON we first develop a suppression-enhancing mask (SEM) based attention to dynamically localize discriminative image regions. More importantly different from existing attention mechanism simply erasing previous discriminative regions our SEM is developed to restrain such regions and then discover other complementary regions by considering the relation between activated regions in a stage-by-stage fashion. In each stage the interactive channel transformation (ICON) module is afterwards designed to exploit correlations across channels of attended activation tensors. Since channels could generally correspond to the parts of fine-grained objects the part correlation can be also modeled accordingly which further improves fine-grained retrieval accuracy. Moreover to be computational economy ICON is realized by an efficient two-step process. Finally the hash learning of our SEMICON consists of both global- and local-level branches for better representing fine-grained objects and then generating binary hash codes explicitly corresponding to multiple levels. Experiments on five benchmark fine-grained datasets show our superiority over competing methods.
