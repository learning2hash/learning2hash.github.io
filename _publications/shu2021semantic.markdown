---
layout: publication
title: Semantic-guided Pixel Sampling For Cloth-changing Person Re-identification
authors: Xiujun Shu, Ge Li, Xiao Wang, Weijian Ruan, Qi Tian
conference: IEEE Signal Processing Letters
year: 2021
bibkey: shu2021semantic
citations: 68
additional_links: [{name: Code, url: 'https://github.com/shuxjweb/pixel_sampling.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.11522'}]
tags: []
short_authors: Shu et al.
---
Cloth-changing person re-identification (re-ID) is a new rising research
topic that aims at retrieving pedestrians whose clothes are changed. This task
is quite challenging and has not been fully studied to date. Current works
mainly focus on body shape or contour sketch, but they are not robust enough
due to view and posture variations. The key to this task is to exploit
cloth-irrelevant cues. This paper proposes a semantic-guided pixel sampling
approach for the cloth-changing person re-ID task. We do not explicitly define
which feature to extract but force the model to automatically learn
cloth-irrelevant cues. Specifically, we first recognize the pedestrian's upper
clothes and pants, then randomly change them by sampling pixels from other
pedestrians. The changed samples retain the identity labels but exchange the
pixels of clothes or pants among different pedestrians. Besides, we adopt a
loss function to constrain the learned features to keep consistent before and
after changes. In this way, the model is forced to learn cues that are
irrelevant to upper clothes and pants. We conduct extensive experiments on the
latest released PRCC dataset. Our method achieved 65.8% on Rank1 accuracy,
which outperforms previous methods with a large margin. The code is available
at https://github.com/shuxjweb/pixel_sampling.git.