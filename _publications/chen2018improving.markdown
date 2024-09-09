---
layout: publication
title: Improving Deep Binary Embedding Networks by Order-aware Reweighting of Triplets
authors: Chen Jikai, Lai Hanjiang, Geng Libing, Pan Yan
conference: "Arxiv"
year: 2018
bibkey: chen2018improving
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1804.06061"}
tags: ['ARXIV', 'Image Retrieval']
---
In this paper we focus on triplet-based deep binary embedding networks for image retrieval task. The triplet loss has been shown to be most effective for the ranking problem. However most of the previous works treat the triplets equally or select the hard triplets based on the loss. Such strategies do not consider the order relations which is important for retrieval task. To this end we propose an order-aware reweighting method to effectively train the triplet-based deep networks which up-weights the important triplets and down-weights the uninformative triplets. First we present the order-aware weighting factors to indicate the importance of the triplets which depend on the rank order of binary codes. Then we reshape the triplet loss to the squared triplet loss such that the loss function will put more weights on the important triplets. Extensive evaluations on four benchmark datasets show that the proposed method achieves significant performance compared with the state-of-the-art baselines.
