---
layout: publication
title: 'Textmountain: Accurate Scene Text Detection Via Instance Segmentation'
authors: Yixing Zhu, Jun Du
conference: Pattern Recognition
year: 2020
bibkey: zhu2018textmountain
citations: 105
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.12786'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Yixing Zhu, Jun Du
---
In this paper, we propose a novel scene text detection method named
TextMountain. The key idea of TextMountain is making full use of border-center
information. Different from previous works that treat center-border as a binary
classification problem, we predict text center-border probability (TCBP) and
text center-direction (TCD). The TCBP is just like a mountain whose top is text
center and foot is text border. The mountaintop can separate text instances
which cannot be easily achieved using semantic segmentation map and its rising
direction can plan a road to top for each pixel on mountain foot at the group
stage. The TCD helps TCBP learning better. Our label rules will not lead to the
ambiguous problem with the transformation of angle, so the proposed method is
robust to multi-oriented text and can also handle well with curved text. In
inference stage, each pixel at the mountain foot needs to search the path to
the mountaintop and this process can be efficiently completed in parallel,
yielding the efficiency of our method compared with others. The experiments on
MLT, ICDAR2015, RCTW-17 and SCUT-CTW1500 databases demonstrate that the
proposed method achieves better or comparable performance in terms of both
accuracy and efficiency. It is worth mentioning our method achieves an
F-measure of 76.85% on MLT which outperforms the previous methods by a large
margin. Code will be made available.