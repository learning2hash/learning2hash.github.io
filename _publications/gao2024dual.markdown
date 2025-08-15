---
layout: publication
title: Dual-modal Prompting For Sketch-based Image Retrieval
authors: Liying Gao, Bingliang Jiao, Peng Wang, Shizhou Zhang, Hanwang Zhang, Yanning
  Zhang
conference: Arxiv
year: 2024
bibkey: gao2024dual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.18695'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Gao et al.
---
Sketch-based image retrieval (SBIR) associates hand-drawn sketches with their
corresponding realistic images. In this study, we aim to tackle two major
challenges of this task simultaneously: i) zero-shot, dealing with unseen
categories, and ii) fine-grained, referring to intra-category instance-level
retrieval. Our key innovation lies in the realization that solely addressing
this cross-category and fine-grained recognition task from the generalization
perspective may be inadequate since the knowledge accumulated from limited seen
categories might not be fully valuable or transferable to unseen target
categories. Inspired by this, in this work, we propose a dual-modal prompting
CLIP (DP-CLIP) network, in which an adaptive prompting strategy is designed.
Specifically, to facilitate the adaptation of our DP-CLIP toward unpredictable
target categories, we employ a set of images within the target category and the
textual category label to respectively construct a set of category-adaptive
prompt tokens and channel scales. By integrating the generated guidance,
DP-CLIP could gain valuable category-centric insights, efficiently adapting to
novel categories and capturing unique discriminative clues for effective
retrieval within each target category. With these designs, our DP-CLIP
outperforms the state-of-the-art fine-grained zero-shot SBIR method by 7.3% in
Acc.@1 on the Sketchy dataset. Meanwhile, in the other two category-level
zero-shot SBIR benchmarks, our method also achieves promising performance.