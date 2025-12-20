---
layout: publication
title: 'SCH-GAN: Semi-supervised Cross-modal Hashing By Generative Adversarial Network'
authors: Jian Zhang, Yuxin Peng, Mingkuan Yuan
conference: IEEE Transactions on Cybernetics
year: 2018
bibkey: zhang2018sch
citations: 132
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.02488'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Supervised", "Unsupervised"]
short_authors: Jian Zhang, Yuxin Peng, Mingkuan Yuan
---
Cross-modal hashing aims to map heterogeneous multimedia data into a common
Hamming space, which can realize fast and flexible retrieval across different
modalities. Supervised cross-modal hashing methods have achieved considerable
progress by incorporating semantic side information. However, they mainly have
two limitations: (1) Heavily rely on large-scale labeled cross-modal training
data which are labor intensive and hard to obtain. (2) Ignore the rich
information contained in the large amount of unlabeled data across different
modalities, especially the margin examples that are easily to be incorrectly
retrieved, which can help to model the correlations. To address these problems,
in this paper we propose a novel Semi-supervised Cross-Modal Hashing approach
by Generative Adversarial Network (SCH-GAN). We aim to take advantage of GAN's
ability for modeling data distributions to promote cross-modal hashing learning
in an adversarial way. The main contributions can be summarized as follows: (1)
We propose a novel generative adversarial network for cross-modal hashing. In
our proposed SCH-GAN, the generative model tries to select margin examples of
one modality from unlabeled data when giving a query of another modality. While
the discriminative model tries to distinguish the selected examples and true
positive examples of the query. These two models play a minimax game so that
the generative model can promote the hashing performance of discriminative
model. (2) We propose a reinforcement learning based algorithm to drive the
training of proposed SCH-GAN. The generative model takes the correlation score
predicted by discriminative model as a reward, and tries to select the examples
close to the margin to promote discriminative model by maximizing the margin
between positive and negative data. Experiments on 3 widely-used datasets
verify the effectiveness of our proposed approach.