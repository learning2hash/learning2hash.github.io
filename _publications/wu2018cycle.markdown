---
layout: publication
title: Cycle-consistent Deep Generative Hashing For Cross-modal Retrieval
authors: Lin Wu, Yang Wang, Ling Shao
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: wu2018cycle
citations: 189
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.11013'}]
tags: ["Hashing Methods", "Multimodal Retrieval", "Robustness", "Scalability"]
short_authors: Lin Wu, Yang Wang, Ling Shao
---
In this paper, we propose a novel deep generative approach to cross-modal
retrieval to learn hash functions in the absence of paired training samples
through the cycle consistency loss. Our proposed approach employs adversarial
training scheme to lean a couple of hash functions enabling translation between
modalities while assuming the underlying semantic relationship. To induce the
hash codes with semantics to the input-output pair, cycle consistency loss is
further proposed upon the adversarial training to strengthen the correlations
between inputs and corresponding outputs. Our approach is generative to learn
hash functions such that the learned hash codes can maximally correlate each
input-output correspondence, meanwhile can also regenerate the inputs so as to
minimize the information loss. The learning to hash embedding is thus performed
to jointly optimize the parameters of the hash functions across modalities as
well as the associated generative models. Extensive experiments on a variety of
large-scale cross-modal data sets demonstrate that our proposed method achieves
better retrieval results than the state-of-the-arts.