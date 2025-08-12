---
layout: publication
title: Boosting Few-shot Fine-grained Recognition With Background Suppression And
  Foreground Alignment
authors: Zican Zha, Hao Tang, Yunlian Sun, Jinhui Tang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2023
bibkey: zha2022boosting
citations: 81
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.01439'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zha et al.
---
Few-shot fine-grained recognition (FS-FGR) aims to recognize novel
fine-grained categories with the help of limited available samples.
Undoubtedly, this task inherits the main challenges from both few-shot learning
and fine-grained recognition. First, the lack of labeled samples makes the
learned model easy to overfit. Second, it also suffers from high intra-class
variance and low inter-class differences in the datasets. To address this
challenging task, we propose a two-stage background suppression and foreground
alignment framework, which is composed of a background activation suppression
(BAS) module, a foreground object alignment (FOA) module, and a local-to-local
(L2L) similarity metric. Specifically, the BAS is introduced to generate a
foreground mask for localization to weaken background disturbance and enhance
dominative foreground objects. The FOA then reconstructs the feature map of
each support sample according to its correction to the query ones, which
addresses the problem of misalignment between support-query image pairs. To
enable the proposed method to have the ability to capture subtle differences in
confused samples, we present a novel L2L similarity metric to further measure
the local similarity between a pair of aligned spatial features in the
embedding space. What's more, considering that background interference brings
poor robustness, we infer the pairwise similarity of feature maps using both
the raw image and the refined image. Extensive experiments conducted on
multiple popular fine-grained benchmarks demonstrate that our method
outperforms the existing state of the art by a large margin. The source codes
are available at: https://github.com/CSer-Tang-hao/BSFA-FSFG.