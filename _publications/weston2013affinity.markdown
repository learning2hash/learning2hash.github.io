---
layout: publication
title: Affinity Weighted Embedding
authors: Jason Weston, Ron Weiss, Hector Yee
conference: Arxiv
year: 2013
bibkey: weston2013affinity
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1301.4171'}]
tags: [Recommender Systems, Evaluation, Datasets, Supervised]
short_authors: Jason Weston, Ron Weiss, Hector Yee
---
Supervised (linear) embedding models like Wsabie and PSI have proven
successful at ranking, recommendation and annotation tasks. However, despite
being scalable to large datasets they do not take full advantage of the extra
data due to their linear nature, and typically underfit. We propose a new class
of models which aim to provide improved performance while retaining many of the
benefits of the existing class of embedding models. Our new approach works by
iteratively learning a linear embedding model where the next iteration's
features and labels are reweighted as a function of the previous iteration. We
describe several variants of the family, and give some initial results.