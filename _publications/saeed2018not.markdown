---
layout: publication
title: 'Not All Embeddings Are Created Equal: Extracting Entity-specific Substructures
  For RDF Graph Embedding'
authors: Muhammad Rizwan Saeed, Charalampos Chelmis, Viktor K. Prasanna
conference: Arxiv
year: 2018
bibkey: saeed2018not
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05184'}]
tags: [Evaluation, Recommender Systems]
short_authors: Muhammad Rizwan Saeed, Charalampos Chelmis, Viktor K. Prasanna
---
Knowledge Graphs (KGs) are becoming essential to information systems that
require access to structured data. Several approaches have been recently
proposed, for obtaining vector representations of KGs suitable for Machine
Learning tasks, based on identifying and extracting relevant graph
substructures using uniform and biased random walks. However, such approaches
lead to representations comprising mostly "popular", instead of "relevant",
entities in the KG. In KGs, in which different types of entities often exist
(such as in Linked Open Data), a given target entity may have its own distinct
set of most "relevant" nodes and edges. We propose specificity as an accurate
measure of identifying most relevant, entity-specific, nodes and edges. We
develop a scalable method based on bidirectional random walks to compute
specificity. Our experimental evaluation results show that specificity-based
biased random walks extract more "meaningful" (in terms of size and relevance)
RDF substructures compared to the state-of-the-art and, the graph embedding
learned from the extracted substructures, outperform existing techniques in the
task of entity recommendation in DBpedia.