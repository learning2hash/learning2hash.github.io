---
layout: publication
title: 'Simans: Simple Ambiguous Negatives Sampling For Dense Text Retrieval'
authors: Kun Zhou, Yeyun Gong, Xiao Liu, Wayne Xin Zhao, Yelong Shen, Anlei Dong,
  Jingwen Lu, Rangan Majumder, Ji-Rong Wen, Nan Duan, Weizhu Chen
conference: 'Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing: Industry Track'
year: 2022
bibkey: zhou2022simans
citations: 23
additional_links: [{name: Code, url: 'https://github.com/microsoft/SimXNS'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.11773'}]
tags: ["EMNLP", "Text Retrieval"]
short_authors: Zhou et al.
---
Sampling proper negatives from a large document pool is vital to effectively
train a dense retrieval model. However, existing negative sampling strategies
suffer from the uninformative or false negative problem. In this work, we
empirically show that according to the measured relevance scores, the negatives
ranked around the positives are generally more informative and less likely to
be false negatives. Intuitively, these negatives are not too hard (*may be
false negatives*) or too easy (*uninformative*). They are the ambiguous
negatives and need more attention during training. Thus, we propose a simple
ambiguous negatives sampling method, SimANS, which incorporates a new sampling
probability distribution to sample more ambiguous negatives. Extensive
experiments on four public and one industry datasets show the effectiveness of
our approach. We made the code and models publicly available in
https://github.com/microsoft/SimXNS.