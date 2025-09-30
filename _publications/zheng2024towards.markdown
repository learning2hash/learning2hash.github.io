---
layout: publication
title: Towards Data Valuation Via Asymmetric Data Shapley
authors: Xi Zheng, Xiangyu Chang, Ruoxi Jia, Yong Tan
conference: Arxiv
year: 2024
bibkey: zheng2024towards
citations: 0
additional_links: [{name: Code, url: 'https://github.com/xzheng01/Asymmetric-Data-Shapley'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.00388'}]
tags: ["Datasets", "Supervised", "Tools & Libraries"]
short_authors: Zheng et al.
---
As data emerges as a vital driver of technological and economic advancements,
a key challenge is accurately quantifying its value in algorithmic
decision-making. The Shapley value, a well-established concept from cooperative
game theory, has been widely adopted to assess the contribution of individual
data sources in supervised machine learning. However, its symmetry axiom
assumes all players in the cooperative game are homogeneous, which overlooks
the complex structures and dependencies present in real-world datasets. To
address this limitation, we extend the traditional data Shapley framework to
asymmetric data Shapley, making it flexible enough to incorporate inherent
structures within the datasets for structure-aware data valuation. We also
introduce an efficient \(k\)-nearest neighbor-based algorithm for its exact
computation. We demonstrate the practical applicability of our framework across
various machine learning tasks and data market contexts. The code is available
at: https://github.com/xzheng01/Asymmetric-Data-Shapley.