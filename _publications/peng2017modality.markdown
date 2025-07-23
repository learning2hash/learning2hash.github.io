---
layout: publication
title: Modality-specific Cross-modal Similarity Measurement With Recurrent Attention
  Network
authors: Peng Yuxin, Qi Jinwei, Yuan Yuxin
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: peng2017modality
citations: 141
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.04776'}]
tags: ["Distance Metric Learning", "Multimodal Retrieval", "Similarity Search"]
short_authors: Peng Yuxin, Qi Jinwei, Yuan Yuxin
---
Nowadays, cross-modal retrieval plays an indispensable role to flexibly find
information across different modalities of data. Effectively measuring the
similarity between different modalities of data is the key of cross-modal
retrieval. Different modalities such as image and text have imbalanced and
complementary relationships, which contain unequal amount of information when
describing the same semantics. For example, images often contain more details
that cannot be demonstrated by textual descriptions and vice versa. Existing
works based on Deep Neural Network (DNN) mostly construct one common space for
different modalities to find the latent alignments between them, which lose
their exclusive modality-specific characteristics. Different from the existing
works, we propose modality-specific cross-modal similarity measurement (MCSM)
approach by constructing independent semantic space for each modality, which
adopts end-to-end framework to directly generate modality-specific cross-modal
similarity without explicit common representation. For each semantic space,
modality-specific characteristics within one modality are fully exploited by
recurrent attention network, while the data of another modality is projected
into this space with attention based joint embedding to utilize the learned
attention weights for guiding the fine-grained cross-modal correlation
learning, which can capture the imbalanced and complementary relationships
between different modalities. Finally, the complementarity between the semantic
spaces for different modalities is explored by adaptive fusion of the
modality-specific cross-modal similarities to perform cross-modal retrieval.
Experiments on the widely-used Wikipedia and Pascal Sentence datasets as well
as our constructed large-scale XMediaNet dataset verify the effectiveness of
our proposed approach, outperforming 9 state-of-the-art methods.