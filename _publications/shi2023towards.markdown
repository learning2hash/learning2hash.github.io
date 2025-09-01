---
layout: publication
title: Towards Faster K-nearest-neighbor Machine Translation
authors: Xiangyu Shi, Yunlong Liang, Jinan Xu, Yufeng Chen
conference: Advances in Artificial Intelligence and Machine Learning
year: 2024
bibkey: shi2023towards
citations: 0
additional_links: [{name: Paper, url: 'https://dx.doi.org/10.54364/AAIML.2024.41111'},
  {name: Paper, url: 'https://arxiv.org/abs/2312.07419'}]
tags: ["Uncategorized"]
short_authors: Shi et al.
---
Recent works have proven the effectiveness of k-nearest-neighbor machine
translation(a.k.a kNN-MT) approaches to produce remarkable improvement in
cross-domain translations. However, these models suffer from heavy retrieve
overhead on the entire datastore when decoding each token. We observe that
during the decoding phase, about 67% to 84% of tokens are unvaried after
searching over the corpus datastore, which means most of the tokens cause
futile retrievals and introduce unnecessary computational costs by initiating
k-nearest-neighbor searches. We consider this phenomenon is explainable in
linguistics and propose a simple yet effective multi-layer perceptron (MLP)
network to predict whether a token should be translated jointly by the neural
machine translation model and probabilities produced by the kNN or just by the
neural model. The results show that our method succeeds in reducing redundant
retrieval operations and significantly reduces the overhead of kNN retrievals
by up to 53% at the expense of a slight decline in translation quality.
Moreover, our method could work together with all existing kNN-MT systems. This
work has been accepted for publication in the jornal Advances in Artificial
Intelligence and Machine Learning (ISSN: 2582-9793). The final published
version can be found at DOI: https://dx.doi.org/10.54364/AAIML.2024.41111