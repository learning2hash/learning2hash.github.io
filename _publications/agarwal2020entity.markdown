---
layout: publication
title: Entity Linking Via Dual And Cross-attention Encoders
authors: Oshin Agarwal, Daniel M. Bikel
conference: Arxiv
year: 2020
bibkey: agarwal2020entity
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.03555'}]
tags: ["Datasets", "Re-Ranking"]
short_authors: Oshin Agarwal, Daniel M. Bikel
---
Entity Linking has two main open areas of research: 1) generate candidate
entities without using alias tables and 2) generate more contextual
representations for both mentions and entities. Recently, a solution has been
proposed for the former as a dual-encoder entity retrieval system (Gillick et
al., 2019) that learns mention and entity representations in the same space,
and performs linking by selecting the nearest entity to the mention in this
space. In this work, we use this retrieval system solely for generating
candidate entities. We then rerank the entities by using a cross-attention
encoder over the target mention and each of the candidate entities. Whereas a
dual encoder approach forces all information to be contained in the small,
fixed set of vector dimensions used to represent mentions and entities, a
crossattention model allows for the use of detailed information (read:
features) from the entirety of each <mention, context, candidate entity> tuple.
We experiment with features used in the reranker including different ways of
incorporating document-level context. We achieve state-of-the-art results on
TACKBP-2010 dataset, with 92.05% accuracy. Furthermore, we show how the
rescoring model generalizes well when trained on the larger CoNLL-2003 dataset
and evaluated on TACKBP-2010.