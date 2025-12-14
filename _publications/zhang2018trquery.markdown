---
layout: publication
title: 'Trquery: An Embedding-based Framework For Recommanding SPARQL Queries'
authors: Lijing Zhang, Xiaowang Zhang, Zhiyong Feng
conference: Arxiv
year: 2018
bibkey: zhang2018trquery
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.06205'}]
tags: [Tools & Libraries, Recommender Systems, Efficiency, Datasets]
short_authors: Lijing Zhang, Xiaowang Zhang, Zhiyong Feng
---
In this paper, we present an embedding-based framework (TrQuery) for
recommending solutions of a SPARQL query, including approximate solutions when
exact querying solutions are not available due to incompleteness or
inconsistencies of real-world RDF data. Within this framework, embedding is
applied to score solutions together with edit distance so that we could obtain
more fine-grained recommendations than those recommendations via edit distance.
For instance, graphs of two querying solutions with a similar structure can be
distinguished in our proposed framework while the edit distance depending on
structural difference becomes unable. To this end, we propose a novel score
model built on vector space generated in embedding system to compute the
similarity between an approximate subgraph matching and a whole graph matching.
Finally, we evaluate our approach on large RDF datasets DBpedia and YAGO, and
experimental results show that TrQuery exhibits an excellent behavior in terms
of both effectiveness and efficiency.