---
layout: publication
title: Efficient Parallel Learning Of Word2vec
authors: Jeroen B. P. Vuurens, Carsten Eickhoff, Arjen P. de Vries
conference: Arxiv
year: 2016
bibkey: vuurens2016efficient
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07822'}]
tags: ["Efficiency"]
short_authors: Jeroen B. P. Vuurens, Carsten Eickhoff, Arjen P. de Vries
---
Since its introduction, Word2Vec and its variants are widely used to learn
semantics-preserving representations of words or entities in an embedding
space, which can be used to produce state-of-art results for various Natural
Language Processing tasks. Existing implementations aim to learn efficiently by
running multiple threads in parallel while operating on a single model in
shared memory, ignoring incidental memory update collisions. We show that these
collisions can degrade the efficiency of parallel learning, and propose a
straightforward caching strategy that improves the efficiency by a factor of 4.