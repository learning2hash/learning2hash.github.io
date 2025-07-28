---
layout: publication
title: Scalable Graph-based Individual Named Entity Identification
authors: Sammy Khalife, Michalis Vazirgiannis
conference: Arxiv
year: 2018
bibkey: khalife2018scalable
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.10547'}]
tags: []
short_authors: Sammy Khalife, Michalis Vazirgiannis
---
Named entity discovery (NED) is an important information retrieval problem
that can be decomposed into two sub-problems. The first sub-problem, named
entity recognition (NER), aims to tag pre-defined sets of words in a vocabulary
(called "named entities": names, places, locations, ...) when they appear in
natural language. The second subproblem, named entity linking/identification
(NEL), considers these entity mentions as queries to be identified in a
pre-existing database. In this paper, we consider the NEL problem, and assume a
set of queries (or mentions) that have to be identified within a knowledge
base. This knowledge base is represented by a text database paired with a
semantic graph. We present state-of-the-art methods in NEL, and propose a
2-step method for individual identification of named entities. Our approach is
well-motivated by the limitations brought by recent deep learning approaches
that lack interpratability, and require lots of parameter tuning along with
large volume of annotated data.
  First of all, we propose a filtering algorithm designed with information
retrieval and text mining techniques, aiming to maximize precision at K
(typically for 5 <= K <=20). Then, we introduce two graph-based methods for
named entity identification to maximize precision at 1 by re-ranking the
remaining top entity candidates. The first identification method is using
parametrized graph mining, and the second similarity with graph kernels. Our
approach capitalizes on a fine-grained classification of entities from
annotated web data. We present our algorithms in details, and show
experimentally on standard datasets (NIST TAC-KBP, CONLL/AIDA) their
performance in terms of precision are better than any graph-based method
reported, and competitive with state-of-the-art systems. Finally, we conclude
on the advantages of our graph-based approach compared to recent deep learning
methods.