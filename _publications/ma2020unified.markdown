---
layout: publication
title: A Unified Model For Recommendation With Selective Neighborhood Modeling
authors: Jingwei Ma, Jiahui Wen, Panpan Zhang, Guangda Zhang, Xue Li
conference: Information Processing &amp; Management
year: 2020
bibkey: ma2020unified
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.08547'}]
tags: ["Recommender Systems"]
short_authors: Ma et al.
---
Neighborhood-based recommenders are a major class of Collaborative Filtering
(CF) models. The intuition is to exploit neighbors with similar preferences for
bridging unseen user-item pairs and alleviating data sparseness. Many existing
works propose neural attention networks to aggregate neighbors and place higher
weights on specific subsets of users for recommendation. However, the
neighborhood information is not necessarily always informative, and the noises
in the neighborhood can negatively affect the model performance. To address
this issue, we propose a novel neighborhood-based recommender, where a hybrid
gated network is designed to automatically separate similar neighbors from
dissimilar (noisy) ones, and aggregate those similar neighbors to comprise
neighborhood representations. The confidence in the neighborhood is also
addressed by putting higher weights on the neighborhood representations if we
are confident with the neighborhood information, and vice versa. In addition, a
user-neighbor component is proposed to explicitly regularize user-neighbor
proximity in the latent space. These two components are combined into a unified
model to complement each other for the recommendation task. Extensive
experiments on three publicly available datasets show that the proposed model
consistently outperforms state-of-the-art neighborhood-based recommenders. We
also study different variants of the proposed model to justify the underlying
intuition of the proposed hybrid gated network and user-neighbor modeling
components.