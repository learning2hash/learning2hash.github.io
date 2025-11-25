---
layout: publication
title: Consensus-aware Visual-semantic Embedding For Image-text Matching
authors: Haoran Wang, Ying Zhang, Zhong Ji, Yanwei Pang, Lin Ma
conference: Lecture Notes in Computer Science
year: 2020
bibkey: wang2020consensus
citations: 162
additional_links: [{name: Code, url: 'https://github.com/BruceW91/CVSE'}, {name: Paper,
    url: 'https://arxiv.org/abs/2007.08883'}]
tags: ["Image Retrieval", "Multimodal Retrieval"]
short_authors: Wang et al.
---
Image-text matching plays a central role in bridging vision and language.
Most existing approaches only rely on the image-text instance pair to learn
their representations, thereby exploiting their matching relationships and
making the corresponding alignments. Such approaches only exploit the
superficial associations contained in the instance pairwise data, with no
consideration of any external commonsense knowledge, which may hinder their
capabilities to reason the higher-level relationships between image and text.
In this paper, we propose a Consensus-aware Visual-Semantic Embedding (CVSE)
model to incorporate the consensus information, namely the commonsense
knowledge shared between both modalities, into image-text matching.
Specifically, the consensus information is exploited by computing the
statistical co-occurrence correlations between the semantic concepts from the
image captioning corpus and deploying the constructed concept correlation graph
to yield the consensus-aware concept (CAC) representations. Afterwards, CVSE
learns the associations and alignments between image and text based on the
exploited consensus as well as the instance-level representations for both
modalities. Extensive experiments conducted on two public datasets verify that
the exploited consensus makes significant contributions to constructing more
meaningful visual-semantic embeddings, with the superior performances over the
state-of-the-art approaches on the bidirectional image and text retrieval task.
Our code of this paper is available at: https://github.com/BruceW91/CVSE.