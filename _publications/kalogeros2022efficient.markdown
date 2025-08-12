---
layout: publication
title: Efficient Query Evaluation Techniques Over Large Amount Of Distributed Linked
  Data
authors: Eleftherios Kalogeros, Manolis Gergatsoulis, Matthew Damigos, Christos Nomikos
conference: Information Systems
year: 2023
bibkey: kalogeros2022efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.05359'}]
tags: ["Evaluation"]
short_authors: Kalogeros et al.
---
As RDF becomes more widely established and the amount of linked data is
rapidly increasing, the efficient querying of large amount of data becomes a
significant challenge. In this paper, we propose a family of algorithms for
querying large amount of linked data in a distributed manner. These query
evaluation algorithms are independent of the way the data is stored, as well as
of the particular implementation of the query evaluation. We then use the
MapReduce paradigm to present a distributed implementation of these algorithms
and experimentally evaluate them, although the algorithms could be
straightforwardly translated into other distributed processing frameworks. We
also investigate and propose multiple query decomposition approaches of Basic
Graph Patterns (subclass of SPARQL queries) that are used to improve the
overall performance of the distributed query answering. A deep analysis of the
effectiveness of these decomposition algorithms is also provided.