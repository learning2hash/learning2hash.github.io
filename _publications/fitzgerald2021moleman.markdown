---
layout: publication
title: 'MOLEMAN: Mention-only Linking Of Entities With A Mention Annotation Network'
authors: Nicholas Fitzgerald, Jan A. Botha, Daniel Gillick, Daniel M. Bikel, Tom Kwiatkowski,
  Andrew McCallum
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 2: Short Papers)'
year: 2021
bibkey: fitzgerald2021moleman
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.07352'}]
tags: [ACL]
short_authors: Fitzgerald et al.
---
We present an instance-based nearest neighbor approach to entity linking. In
contrast to most prior entity retrieval systems which represent each entity
with a single vector, we build a contextualized mention-encoder that learns to
place similar mentions of the same entity closer in vector space than mentions
of different entities. This approach allows all mentions of an entity to serve
as "class prototypes" as inference involves retrieving from the full set of
labeled entity mentions in the training set and applying the nearest mention
neighbor's entity label. Our model is trained on a large multilingual corpus of
mention pairs derived from Wikipedia hyperlinks, and performs nearest neighbor
inference on an index of 700 million mentions. It is simpler to train, gives
more interpretable predictions, and outperforms all other systems on two
multilingual entity linking benchmarks.