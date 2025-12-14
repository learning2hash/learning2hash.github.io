---
layout: publication
title: 'GREN: Graph-regularized Embedding Network For Weakly-supervised Disease Localization
  In X-ray Images'
authors: Baolian Qi, Gangming Zhao, Xin Wei, Changde Du, Chengwei Pan, Yizhou Yu,
  Jinpeng Li
conference: Arxiv
year: 2021
bibkey: qi2021gren
citations: 0
additional_links: [{name: Code, url: 'https://github.com/qibaolian/GREN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2107.06442'}]
tags: [Supervised, Datasets]
short_authors: Qi et al.
---
Locating diseases in chest X-ray images with few careful annotations saves
large human effort. Recent works approached this task with innovative
weakly-supervised algorithms such as multi-instance learning (MIL) and class
activation maps (CAM), however, these methods often yield inaccurate or
incomplete regions. One of the reasons is the neglection of the pathological
implications hidden in the relationship across anatomical regions within each
image and the relationship across images. In this paper, we argue that the
cross-region and cross-image relationship, as contextual and compensating
information, is vital to obtain more consistent and integral regions. To model
the relationship, we propose the Graph Regularized Embedding Network (GREN),
which leverages the intra-image and inter-image information to locate diseases
on chest X-ray images. GREN uses a pre-trained U-Net to segment the lung lobes,
and then models the intra-image relationship between the lung lobes using an
intra-image graph to compare different regions. Meanwhile, the relationship
between in-batch images is modeled by an inter-image graph to compare multiple
images. This process mimics the training and decision-making process of a
radiologist: comparing multiple regions and images for diagnosis. In order for
the deep embedding layers of the neural network to retain structural
information (important in the localization task), we use the Hash coding and
Hamming distance to compute the graphs, which are used as regularizers to
facilitate training. By means of this, our approach achieves the
state-of-the-art result on NIH chest X-ray dataset for weakly-supervised
disease localization. Our codes are accessible online
(https://github.com/qibaolian/GREN).