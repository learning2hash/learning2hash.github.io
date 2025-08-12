---
layout: publication
title: Specialising Word Vectors For Lexical Entailment
authors: "Ivan Vuli\u0107, Nikola Mrk\u0161i\u0107"
conference: 'Proceedings of the 2018 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies, Volume 1
  (Long Papers)'
year: 2018
bibkey: "vuli\u01072017specialising"
citations: 100
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.06371'}]
tags: []
short_authors: "Ivan Vuli\u0107, Nikola Mrk\u0161i\u0107"
---
We present LEAR (Lexical Entailment Attract-Repel), a novel post-processing
method that transforms any input word vector space to emphasise the asymmetric
relation of lexical entailment (LE), also known as the IS-A or
hyponymy-hypernymy relation. By injecting external linguistic constraints
(e.g., WordNet links) into the initial vector space, the LE specialisation
procedure brings true hyponymy-hypernymy pairs closer together in the
transformed Euclidean space. The proposed asymmetric distance measure adjusts
the norms of word vectors to reflect the actual WordNet-style hierarchy of
concepts. Simultaneously, a joint objective enforces semantic similarity using
the symmetric cosine distance, yielding a vector space specialised for both
lexical relations at once. LEAR specialisation achieves state-of-the-art
performance in the tasks of hypernymy directionality, hypernymy detection, and
graded lexical entailment, demonstrating the effectiveness and robustness of
the proposed asymmetric specialisation model.