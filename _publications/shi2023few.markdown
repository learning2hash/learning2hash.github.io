---
layout: publication
title: Few-shot Shape Recognition By Learning Deep Shape-aware Features
authors: Wenlong Shi, Changsheng Lu, Ming Shao, Yinjie Zhang, Siyu Xia, Piotr Koniusz
conference: Arxiv
year: 2023
bibkey: shi2023few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.01315'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Shi et al.
---
Traditional shape descriptors have been gradually replaced by convolutional
neural networks due to their superior performance in feature extraction and
classification. The state-of-the-art methods recognize object shapes via image
reconstruction or pixel classification. However , these methods are biased
toward texture information and overlook the essential shape descriptions, thus,
they fail to generalize to unseen shapes. We are the first to propose a fewshot
shape descriptor (FSSD) to recognize object shapes given only one or a few
samples. We employ an embedding module for FSSD to extract
transformation-invariant shape features. Secondly, we develop a dual attention
mechanism to decompose and reconstruct the shape features via learnable shape
primitives. In this way, any shape can be formed through a finite set basis,
and the learned representation model is highly interpretable and extendable to
unseen shapes. Thirdly, we propose a decoding module to include the supervision
of shape masks and edges and align the original and reconstructed shape
features, enforcing the learned features to be more shape-aware. Lastly, all
the proposed modules are assembled into a few-shot shape recognition scheme.
Experiments on five datasets show that our FSSD significantly improves the
shape classification compared to the state-of-the-art under the few-shot
setting.