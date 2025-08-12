---
layout: publication
title: Matching Entities Across Different Knowledge Graphs With Graph Embeddings
authors: Michael Azmy, Peng Shi, Jimmy Lin, Ihab F. Ilyas
conference: Arxiv
year: 2019
bibkey: azmy2019matching
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.06607'}]
tags: ["Datasets", "Scalability"]
short_authors: Azmy et al.
---
This paper explores the problem of matching entities across different
knowledge graphs. Given a query entity in one knowledge graph, we wish to find
the corresponding real-world entity in another knowledge graph. We formalize
this problem and present two large-scale datasets for this task based on
exiting cross-ontology links between DBpedia and Wikidata, focused on several
hundred thousand ambiguous entities. Using a classification-based approach, we
find that a simple multi-layered perceptron based on representations derived
from RDF2Vec graph embeddings of entities in each knowledge graph is sufficient
to achieve high accuracy, with only small amounts of training data. The
contributions of our work are datasets for examining this problem and strong
baselines on which future work can be based.