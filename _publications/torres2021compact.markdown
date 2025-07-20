---
layout: publication
title: Compact and Effective Representations for Sketch-based Image Retrieval
authors: Torres Pablo, Saavedra Jose M.
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: torres2021compact
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.10278'}]
tags: [CVPR, Image Retrieval]
---
Sketch-based image retrieval (SBIR) has undergone an increasing interest in
the community of computer vision bringing high impact in real applications. For
instance, SBIR brings an increased benefit to eCommerce search engines because
it allows users to formulate a query just by drawing what they need to buy.
However, current methods showing high precision in retrieval work in a high
dimensional space, which negatively affects aspects like memory consumption and
time processing. Although some authors have also proposed compact
representations, these drastically degrade the performance in a low dimension.
Therefore in this work, we present different results of evaluating methods for
producing compact embeddings in the context of sketch-based image retrieval.
Our main interest is in strategies aiming to keep the local structure of the
original space. The recent unsupervised local-topology preserving dimension
reduction method UMAP fits our requirements and shows outstanding performance,
improving even the precision achieved by SOTA methods. We evaluate six methods
in two different datasets. We use Flickr15K and eCommerce datasets; the latter
is another contribution of this work. We show that UMAP allows us to have
feature vectors of 16 bytes improving precision by more than 35%.