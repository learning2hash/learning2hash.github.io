---
layout: publication
title: Reflection Invariance Learning For Few-shot Semantic Segmentation
authors: Qinglong Cao, Yuntian Chen, Chao Ma, Xiaokang Yang
conference: Arxiv
year: 2023
bibkey: cao2023reflection
citations: 0
additional_links: [{name: Code, url: 'https://anonymous.4open.science/r/RILFS-A4D1'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.15850'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Cao et al.
---
Few-shot semantic segmentation (FSS) aims to segment objects of unseen
classes in query images with only a few annotated support images. Existing FSS
algorithms typically focus on mining category representations from the
single-view support to match semantic objects of the single-view query.
However, the limited annotated samples render the single-view matching struggle
to perceive the reflection invariance of novel objects, which results in a
restricted learning space for novel categories and further induces a biased
segmentation with demoted parsing performance. To address this challenge, this
paper proposes a fresh few-shot segmentation framework to mine the reflection
invariance in a multi-view matching manner. Specifically, original and
reflection support features from different perspectives with the same semantics
are learnable fused to obtain the reflection invariance prototype with a
stronger category representation ability. Simultaneously, aiming at providing
better prior guidance, the Reflection Invariance Prior Mask Generation (RIPMG)
module is proposed to integrate prior knowledge from different perspectives.
Finally, segmentation predictions from varying views are complementarily merged
in the Reflection Invariance Semantic Prediction (RISP) module to yield precise
segmentation predictions. Extensive experiments on both PASCAL-\(5^\textit\{i\}\)
and COCO-\(20^\textit\{i\}\) datasets demonstrate the effectiveness of our approach
and show that our method could achieve state-of-the-art performance. Code is
available at https://anonymous.4open.science/r/RILFS-A4D1