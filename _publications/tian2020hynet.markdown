---
layout: publication
title: 'Hynet: Learning Local Descriptor With Hybrid Similarity Measure And Triplet
  Loss'
authors: Tian Yurun, Barroso-laguna Axel, Ng Tony, Balntas Vassileios, Mikolajczyk
  Krystian
conference: Arxiv
year: 2020
bibkey: tian2020hynet
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.10202'}]
tags: ["Distance-Metric-Learning"]
short_authors: Tian et al.
---
Recent works show that local descriptor learning benefits from the use of L2
normalisation, however, an in-depth analysis of this effect lacks in the
literature. In this paper, we investigate how L2 normalisation affects the
back-propagated descriptor gradients during training. Based on our
observations, we propose HyNet, a new local descriptor that leads to
state-of-the-art results in matching. HyNet introduces a hybrid similarity
measure for triplet margin loss, a regularisation term constraining the
descriptor norm, and a new network architecture that performs L2 normalisation
of all intermediate feature maps and the output descriptors. HyNet surpasses
previous methods by a significant margin on standard benchmarks that include
patch matching, verification, and retrieval, as well as outperforming full
end-to-end methods on 3D reconstruction tasks.