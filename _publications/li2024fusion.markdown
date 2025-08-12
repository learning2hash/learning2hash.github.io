---
layout: publication
title: 'Fusion Makes Perfection: An Efficient Multi-grained Matching Approach For
  Zero-shot Relation Extraction'
authors: Shilong Li, Ge Bai, Zhang Zhang, Ying Liu, Chenji Lu, Daichi Guo, Ruifang
  Liu, Yong Sun
conference: 'Proceedings of the 2024 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies (Volume 2:
  Short Papers)'
year: 2024
bibkey: li2024fusion
citations: 1
additional_links: [{name: Code, url: 'https://github.com/longls777/EMMA'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.11429'}]
tags: ["Efficiency", "NAACL"]
short_authors: Li et al.
---
Predicting unseen relations that cannot be observed during the training phase
is a challenging task in relation extraction. Previous works have made progress
by matching the semantics between input instances and label descriptions.
However, fine-grained matching often requires laborious manual annotation, and
rich interactions between instances and label descriptions come with
significant computational overhead. In this work, we propose an efficient
multi-grained matching approach that uses virtual entity matching to reduce
manual annotation cost, and fuses coarse-grained recall and fine-grained
classification for rich interactions with guaranteed inference speed.
Experimental results show that our approach outperforms the previous State Of
The Art (SOTA) methods, and achieves a balance between inference efficiency and
prediction accuracy in zero-shot relation extraction tasks. Our code is
available at https://github.com/longls777/EMMA.