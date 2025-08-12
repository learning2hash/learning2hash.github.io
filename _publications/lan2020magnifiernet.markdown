---
layout: publication
title: 'Magnifiernet: Towards Semantic Adversary And Fusion For Person Re-identification'
authors: Yushi Lan, Yuan Liu, Maoqing Tian, Xinchi Zhou, Xuesen Zhang, Shuai Yi, Hongsheng
  Li
conference: Proceedings of the British Machine Vision Conference 2020
year: 2020
bibkey: lan2020magnifiernet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10979'}]
tags: ["Robustness"]
short_authors: Lan et al.
---
Although person re-identification (ReID) has achieved significant improvement
recently by enforcing part alignment, it is still a challenging task when it
comes to distinguishing visually similar identities or identifying the occluded
person. In these scenarios, magnifying details in each part features and
selectively fusing them together may provide a feasible solution. In this work,
we propose MagnifierNet, a triple-branch network which accurately mines details
from whole to parts. Firstly, the holistic salient features are encoded by a
global branch. Secondly, to enhance detailed representation for each semantic
region, the "Semantic Adversarial Branch" is designed to learn from dynamically
generated semantic-occluded samples during training. Meanwhile, we introduce
"Semantic Fusion Branch" to filter out irrelevant noises by selectively fusing
semantic region information sequentially. To further improve feature diversity,
we introduce a novel loss function "Semantic Diversity Loss" to remove
redundant overlaps across learned semantic representations. State-of-the-art
performance has been achieved on three benchmarks by large margins.
Specifically, the mAP score is improved by 6% and 5% on the most challenging
CUHK03-L and CUHK03-D benchmarks.