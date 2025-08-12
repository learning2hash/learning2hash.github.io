---
layout: publication
title: Improving Entity Linking Through Semantic Reinforced Entity Embeddings
authors: Feng Hou, Ruili Wang, Jun He, Yi Zhou
conference: Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics
year: 2020
bibkey: hou2020improving
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.08495'}]
tags: ["Evaluation"]
short_authors: Hou et al.
---
Entity embeddings, which represent different aspects of each entity with a
single vector like word embeddings, are a key component of neural entity
linking models. Existing entity embeddings are learned from canonical Wikipedia
articles and local contexts surrounding target entities. Such entity embeddings
are effective, but too distinctive for linking models to learn contextual
commonality. We propose a simple yet effective method, FGS2EE, to inject
fine-grained semantic information into entity embeddings to reduce the
distinctiveness and facilitate the learning of contextual commonality. FGS2EE
first uses the embeddings of semantic type words to generate semantic
embeddings, and then combines them with existing entity embeddings through
linear aggregation. Extensive experiments show the effectiveness of such
embeddings. Based on our entity embeddings, we achieved new sate-of-the-art
performance on entity linking.