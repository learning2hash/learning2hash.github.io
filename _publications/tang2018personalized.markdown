---
layout: publication
title: Personalized Top-n Sequential Recommendation Via Convolutional Sequence Embedding
authors: Jiaxi Tang, Ke Wang
conference: Proceedings of the Eleventh ACM International Conference on Web Search
  and Data Mining
year: 2018
bibkey: tang2018personalized
citations: 1547
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.07426'}]
tags: ["Recommender Systems"]
short_authors: Jiaxi Tang, Ke Wang
---
Top-\(N\) sequential recommendation models each user as a sequence of items
interacted in the past and aims to predict top-\(N\) ranked items that a user
will likely interact in a `near future'. The order of interaction implies that
sequential patterns play an important role where more recent items in a
sequence have a larger impact on the next item. In this paper, we propose a
Convolutional Sequence Embedding Recommendation Model (*Caser*) as a
solution to address this requirement. The idea is to embed a sequence of recent
items into an `image' in the time and latent spaces and learn sequential
patterns as local features of the image using convolutional filters. This
approach provides a unified and flexible network structure for capturing both
general preferences and sequential patterns. The experiments on public datasets
demonstrated that Caser consistently outperforms state-of-the-art sequential
recommendation methods on a variety of common evaluation metrics.