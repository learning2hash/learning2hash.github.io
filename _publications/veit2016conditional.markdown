---
layout: publication
title: Conditional Similarity Networks
authors: Andreas Veit, Serge Belongie, Theofanis Karaletsos
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: veit2016conditional
citations: 99
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.07810'}]
tags: ["CVPR"]
short_authors: Andreas Veit, Serge Belongie, Theofanis Karaletsos
---
What makes images similar? To measure the similarity between images, they are
typically embedded in a feature-vector space, in which their distance preserve
the relative dissimilarity. However, when learning such similarity embeddings
the simplifying assumption is commonly made that images are only compared to
one unique measure of similarity. A main reason for this is that contradicting
notions of similarities cannot be captured in a single space. To address this
shortcoming, we propose Conditional Similarity Networks (CSNs) that learn
embeddings differentiated into semantically distinct subspaces that capture the
different notions of similarities. CSNs jointly learn a disentangled embedding
where features for different similarities are encoded in separate dimensions as
well as masks that select and reweight relevant dimensions to induce a subspace
that encodes a specific similarity notion. We show that our approach learns
interpretable image representations with visually relevant semantic subspaces.
Further, when evaluating on triplet questions from multiple similarity notions
our model even outperforms the accuracy obtained by training individual
specialized networks for each notion separately.