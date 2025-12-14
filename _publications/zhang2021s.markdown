---
layout: publication
title: 'S-simcse: Sampled Sub-networks For Contrastive Learning Of Sentence Embedding'
authors: Junlei Zhang, Zhenzhong Lan
conference: Arxiv
year: 2021
bibkey: zhang2021s
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.11750'}]
tags: [Evaluation, Datasets, Self-Supervised]
short_authors: Junlei Zhang, Zhenzhong Lan
---
Contrastive learning has been studied for improving the performance of
learning sentence embeddings. The current state-of-the-art method is the
SimCSE, which takes dropout as the data augmentation method and feeds a
pre-trained transformer encoder the same input sentence twice. The
corresponding outputs, two sentence embeddings derived from the same sentence
with different dropout masks, can be used to build a positive pair. A network
being applied with a dropout mask can be regarded as a sub-network of itsef,
whose expected scale is determined by the dropout rate. In this paper, we push
sub-networks with different expected scales learn similar embedding for the
same sentence. SimCSE failed to do so because they fixed the dropout rate to a
tuned hyperparameter. We achieve this by sampling dropout rate from a
distribution eatch forward process. As this method may make optimization
harder, we also propose a simple sentence-wise mask strategy to sample more
sub-networks. We evaluated the proposed S-SimCSE on several popular semantic
text similarity datasets. Experimental results show that S-SimCSE outperforms
the state-of-the-art SimCSE more than \(1%\) on BERT\(_\{base\}\)