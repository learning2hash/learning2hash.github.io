---
layout: publication
title: Deep Multiple Instance Learning With Distance-aware Self-attention
authors: "Georg W\xF6lflein, Lucie Charlotte Magister, Pietro Li\xF2, David J. Harrison,\
  \ Ognjen Arandjelovi\u0107"
conference: Arxiv
year: 2023
bibkey: "w\xF6lflein2023deep"
citations: 0
additional_links: [{name: Code, url: 'https://anonymous.4open.science/r/das-mil'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.10552'}]
tags: []
short_authors: "W\xF6lflein et al."
---
Traditional supervised learning tasks require a label for every instance in
the training set, but in many real-world applications, labels are only
available for collections (bags) of instances. This problem setting, known as
multiple instance learning (MIL), is particularly relevant in the medical
domain, where high-resolution images are split into smaller patches, but labels
apply to the image as a whole. Recent MIL models are able to capture
correspondences between patches by employing self-attention, allowing them to
weigh each patch differently based on all other patches in the bag. However,
these approaches still do not consider the relative spatial relationships
between patches within the larger image, which is especially important in
computational pathology. To this end, we introduce a novel MIL model with
distance-aware self-attention (DAS-MIL), which explicitly takes into account
relative spatial information when modelling the interactions between patches.
Unlike existing relative position representations for self-attention which are
discrete, our approach introduces continuous distance-dependent terms into the
computation of the attention weights, and is the first to apply relative
position representations in the context of MIL. We evaluate our model on a
custom MNIST-based MIL dataset that requires the consideration of relative
spatial information, as well as on CAMELYON16, a publicly available cancer
metastasis detection dataset, where we achieve a test AUROC score of 0.91. On
both datasets, our model outperforms existing MIL approaches that employ
absolute positional encodings, as well as existing relative position
representation schemes applied to MIL. Our code is available at
https://anonymous.4open.science/r/das-mil.