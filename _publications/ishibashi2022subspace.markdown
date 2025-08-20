---
layout: publication
title: Subspace Representations For Soft Set Operations And Sentence Similarities
authors: Yoichi Ishibashi, Sho Yokoi, Katsuhito Sudoh, Satoshi Nakamura
conference: 'Proceedings of the 2024 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies (Volume 1:
  Long Papers)'
year: 2024
bibkey: ishibashi2022subspace
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.13034'}]
tags: [NAACL, ACL]
short_authors: Ishibashi et al.
---
In the field of natural language processing (NLP), continuous vector
representations are crucial for capturing the semantic meanings of individual
words. Yet, when it comes to the representations of sets of words, the
conventional vector-based approaches often struggle with expressiveness and
lack the essential set operations such as union, intersection, and complement.
Inspired by quantum logic, we realize the representation of word sets and
corresponding set operations within pre-trained word embedding spaces. By
grounding our approach in the linear subspaces, we enable efficient computation
of various set operations and facilitate the soft computation of membership
functions within continuous spaces. Moreover, we allow for the computation of
the F-score directly within word vectors, thereby establishing a direct link to
the assessment of sentence similarity. In experiments with widely-used
pre-trained embeddings and benchmarks, we show that our subspace-based set
operations consistently outperform vector-based ones in both sentence
similarity and set retrieval tasks.