---
layout: publication
title: Do Similar Entities Have Similar Embeddings?
authors: Nicolas Hubert, Heiko Paulheim, Armelle Brun, Davy Monticolo
conference: Lecture Notes in Computer Science
year: 2023
bibkey: hubert2023do
citations: 4
additional_links: [{name: Code, url: 'https://github.com/nicolas-hbt/similar-embeddings/'},
  {name: Paper, url: 'https://arxiv.org/abs/2312.10370'}]
tags: ["Datasets", "Recommender Systems"]
short_authors: Hubert et al.
---
Knowledge graph embedding models (KGEMs) developed for link prediction learn
vector representations for entities in a knowledge graph, known as embeddings.
A common tacit assumption is the KGE entity similarity assumption, which states
that these KGEMs retain the graph's structure within their embedding space,
\textit\{i.e.\}, position similar entities within the graph close to one another.
This desirable property make KGEMs widely used in downstream tasks such as
recommender systems or drug repurposing. Yet, the relation of entity similarity
and similarity in the embedding space has rarely been formally evaluated.
Typically, KGEMs are assessed based on their sole link prediction capabilities,
using ranked-based metrics such as Hits@K or Mean Rank. This paper challenges
the prevailing assumption that entity similarity in the graph is inherently
mirrored in the embedding space. Therefore, we conduct extensive experiments to
measure the capability of KGEMs to cluster similar entities together, and
investigate the nature of the underlying factors. Moreover, we study if
different KGEMs expose a different notion of similarity. Datasets, pre-trained
embeddings and code are available at:
https://github.com/nicolas-hbt/similar-embeddings/.