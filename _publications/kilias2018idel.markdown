---
layout: publication
title: 'IDEL: In-database Entity Linking With Neural Embeddings'
authors: "Kilias Torsten, L\xF6ser Alexander, Gers Felix A., Koopmanschap Richard,\
  \ Zhang Ying, Kersten Martin"
conference: Arxiv
year: 2018
bibkey: kilias2018idel
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.04884'}]
tags: ["Efficiency", "Neural Hashing", "Similarity Search", "Vector Indexing"]
short_authors: Kilias et al.
---
We present a novel architecture, In-Database Entity Linking (IDEL), in which
we integrate the analytics-optimized RDBMS MonetDB with neural text mining
abilities. Our system design abstracts core tasks of most neural entity linking
systems for MonetDB. To the best of our knowledge, this is the first defacto
implemented system integrating entity-linking in a database. We leverage the
ability of MonetDB to support in-database-analytics with user defined functions
(UDFs) implemented in Python. These functions call machine learning libraries
for neural text mining, such as TensorFlow. The system achieves zero cost for
data shipping and transformation by utilizing MonetDB's ability to embed Python
processes in the database kernel and exchange data in NumPy arrays. IDEL
represents text and relational data in a joint vector space with neural
embeddings and can compensate errors with ambiguous entity representations. For
detecting matching entities, we propose a novel similarity function based on
joint neural embeddings which are learned via minimizing pairwise contrastive
ranking loss. This function utilizes a high dimensional index structures for
fast retrieval of matching entities. Our first implementation and experiments
using the WebNLG corpus show the effectiveness and the potentials of IDEL.