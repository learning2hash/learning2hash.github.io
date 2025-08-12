---
layout: publication
title: Walk This Way! Entity Walks And Property Walks For Rdf2vec
authors: Jan Portisch, Heiko Paulheim
conference: Arxiv
year: 2022
bibkey: portisch2022walk
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.02777'}]
tags: ["Evaluation"]
short_authors: Jan Portisch, Heiko Paulheim
---
RDF2vec is a knowledge graph embedding mechanism which first extracts
sequences from knowledge graphs by performing random walks, then feeds those
into the word embedding algorithm word2vec for computing vector representations
for entities. In this poster, we introduce two new flavors of walk extraction
coined e-walks and p-walks, which put an emphasis on the structure or the
neighborhood of an entity respectively, and thereby allow for creating
embeddings which focus on similarity or relatedness. By combining the walk
strategies with order-aware and classic RDF2vec, as well as CBOW and skip-gram
word2vec embeddings, we conduct a preliminary evaluation with a total of 12
RDF2vec variants.