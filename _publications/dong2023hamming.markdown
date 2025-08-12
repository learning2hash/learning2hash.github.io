---
layout: publication
title: 'Hamming Encoder: Mining Discriminative K-mers For Discrete Sequence Classification'
authors: Junjie Dong, Mudi Jiang, Lianyu Hu, Zengyou He
conference: Data Mining and Knowledge Discovery
year: 2025
bibkey: dong2023hamming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.10321'}]
tags: []
short_authors: Dong et al.
---
Sequence classification has numerous applications in various fields. Despite
extensive studies in the last decades, many challenges still exist,
particularly in pattern-based methods. Existing pattern-based methods measure
the discriminative power of each feature individually during the mining
process, leading to the result of missing some combinations of features with
discriminative power. Furthermore, it is difficult to ensure the overall
discriminative performance after converting sequences into feature vectors. To
address these challenges, we propose a novel approach called Hamming Encoder,
which utilizes a binarized 1D-convolutional neural network (1DCNN) architecture
to mine discriminative k-mer sets. In particular, we adopt a Hamming
distance-based similarity measure to ensure consistency in the feature mining
and classification procedure. Our method involves training an interpretable CNN
encoder for sequential data and performing a gradient-based search for
discriminative k-mer combinations. Experiments show that the Hamming Encoder
method proposed in this paper outperforms existing state-of-the-art methods in
terms of classification accuracy.