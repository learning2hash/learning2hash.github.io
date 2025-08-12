---
layout: publication
title: Improving Entity Retrieval On Structured Data
authors: Besnik Fetahu, Ujwal Gadiraju, Stefan Dietze
conference: Lecture Notes in Computer Science
year: 2015
bibkey: fetahu2015improving
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.10349'}]
tags: []
short_authors: Besnik Fetahu, Ujwal Gadiraju, Stefan Dietze
---
The increasing amount of data on the Web, in particular of Linked Data, has
led to a diverse landscape of datasets, which make entity retrieval a
challenging task. Explicit cross-dataset links, for instance to indicate
co-references or related entities can significantly improve entity retrieval.
However, only a small fraction of entities are interlinked through explicit
statements. In this paper, we propose a two-fold entity retrieval approach. In
a first, offline preprocessing step, we cluster entities based on the
*x--means* and *spectral* clustering algorithms. In the second step,
we propose an optimized retrieval model which takes advantage of our
precomputed clusters. For a given set of entities retrieved by the BM25F
retrieval approach and a given user query, we further expand the result set
with relevant entities by considering features of the queries, entities and the
precomputed clusters. Finally, we re-rank the expanded result set with respect
to the relevance to the query. We perform a thorough experimental evaluation on
the Billions Triple Challenge (BTC12) dataset. The proposed approach shows
significant improvements compared to the baseline and state of the art
approaches.