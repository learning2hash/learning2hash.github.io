---
layout: publication
title: Functional Hashing For Compressing Neural Networks
authors: Shi Lei, Feng Shikun, Zhu Zhifan
conference: "Arxiv"
year: 2016
bibkey: shi2016functional
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.06560"}
tags: ['ARXIV', 'Supervised']
---
As the complexity of deep neural networks (DNNs) trend to grow to absorb the increasing sizes of data memory and energy consumption has been receiving more and more attentions for industrial applications especially on mobile devices. This paper presents a novel structure based on functional hashing to compress DNNs namely FunHashNN. For each entry in a deep net FunHashNN uses multiple low-cost hash functions to fetch values in the compression space and then employs a small reconstruction network to recover that entry. The reconstruction network is plugged into the whole network and trained jointly. FunHashNN includes the recently proposed HashedNets as a degenerated case and benefits from larger value capacity and less reconstruction loss. We further discuss extensions with dual space hashing and multi-hops. On several benchmark datasets FunHashNN demonstrates high compression ratios with little loss on prediction accuracy.
