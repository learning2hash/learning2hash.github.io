---
layout: publication
title: Multiple Discrimination And Pairwise CNN For View-based 3D Object Retrieval
authors: Z. Gao, K. X Xue, S. H Wan
conference: Neural Networks
year: 2020
bibkey: gao2020multiple
citations: 86
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11977'}]
tags: ["Distance Metric Learning", "Evaluation", "Neural Hashing", "Scalability"]
short_authors: Z. Gao, K. X Xue, S. H Wan
---
With the rapid development and wide application of computer, camera device,
network and hardware technology, 3D object (or model) retrieval has attracted
widespread attention and it has become a hot research topic in the computer
vision domain. Deep learning features already available in 3D object retrieval
have been proven to be better than the retrieval performance of hand-crafted
features. However, most existing networks do not take into account the impact
of multi-view image selection on network training, and the use of contrastive
loss alone only forcing the same-class samples to be as close as possible. In
this work, a novel solution named Multi-view Discrimination and Pairwise CNN
(MDPCNN) for 3D object retrieval is proposed to tackle these issues. It can
simultaneously input of multiple batches and multiple views by adding the Slice
layer and the Concat layer. Furthermore, a highly discriminative network is
obtained by training samples that are not easy to be classified by clustering.
Lastly, we deploy the contrastive-center loss and contrastive loss as the
optimization objective that has better intra-class compactness and inter-class
separability. Large-scale experiments show that the proposed MDPCNN can achieve
a significant performance over the state-of-the-art algorithms in 3D object
retrieval.