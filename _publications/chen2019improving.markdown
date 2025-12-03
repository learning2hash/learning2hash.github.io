---
layout: publication
title: Improving Distantly-supervised Entity Typing With Compact Latent Space Clustering
authors: Bo Chen, Xiaotao Gu, Yufeng Hu, Siliang Tang, Guoping Hu, Yueting Zhuang,
  Xiang Ren
conference: Proceedings of the 2019 Conference of the North
year: 2019
bibkey: chen2019improving
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.06475'}]
tags: ["Efficiency", "Evaluation", "Supervised"]
short_authors: Chen et al.
---
Recently, distant supervision has gained great success on Fine-grained Entity
Typing (FET). Despite its efficiency in reducing manual labeling efforts, it
also brings the challenge of dealing with false entity type labels, as distant
supervision assigns labels in a context agnostic manner. Existing works
alleviated this issue with partial-label loss, but usually suffer from
confirmation bias, which means the classifier fit a pseudo data distribution
given by itself. In this work, we propose to regularize distantly supervised
models with Compact Latent Space Clustering (CLSC) to bypass this problem and
effectively utilize noisy data yet. Our proposed method first dynamically
constructs a similarity graph of different entity mentions; infer the labels of
noisy instances via label propagation. Based on the inferred labels, mention
embeddings are updated accordingly to encourage entity mentions with close
semantics to form a compact cluster in the embedding space,thus leading to
better classification performance. Extensive experiments on standard benchmarks
show that our CLSC model consistently outperforms state-of-the-art distantly
supervised entity typing systems by a significant margin.