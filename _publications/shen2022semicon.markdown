---
layout: publication
title: SEMICON A Learning45;to45;hash Solution For Large45;scale Fine45;grained Image Retrieval
authors: Shen Yang, Sun Xuhao, Wei Xiu-shen, Jiang Qing-yuan, Yang Jian
conference: "Arxiv"
year: 2022
bibkey: shen2022semicon
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2209.13833"}
tags: ['ARXIV', 'Image Retrieval', 'Independent']
---
In this paper we propose Suppression45;Enhancing Mask based attention and Interactive Channel transformatiON (SEMICON) to learn binary hash codes for dealing with large45;scale fine45;grained image retrieval tasks. In SEMICON we first develop a suppression45;enhancing mask (SEM) based attention to dynamically localize discriminative image regions. More importantly different from existing attention mechanism simply erasing previous discriminative regions our SEM is developed to restrain such regions and then discover other complementary regions by considering the relation between activated regions in a stage45;by45;stage fashion. In each stage the interactive channel transformation (ICON) module is afterwards designed to exploit correlations across channels of attended activation tensors. Since channels could generally correspond to the parts of fine45;grained objects the part correlation can be also modeled accordingly which further improves fine45;grained retrieval accuracy. Moreover to be computational economy ICON is realized by an efficient two45;step process. Finally the hash learning of our SEMICON consists of both global45; and local45;level branches for better representing fine45;grained objects and then generating binary hash codes explicitly corresponding to multiple levels. Experiments on five benchmark fine45;grained datasets show our superiority over competing methods.
