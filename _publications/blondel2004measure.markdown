---
layout: publication
title: A Measure Of Similarity Between Graph Vertices
authors: Vincent Blondel, Anahi Gajardo, Maureen Heymans, Pierre Senellart, Paul van
  Dooren
conference: Arxiv
year: 2004
bibkey: blondel2004measure
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0407061'}]
tags: ["Distance Metric Learning", "Graph Based ANN", "Similarity Search"]
short_authors: Blondel et al.
---
We introduce a concept of similarity between vertices of directed graphs. Let
G_A and G_B be two directed graphs. We define a similarity matrix whose (i,
j)-th real entry expresses how similar vertex j (in G_A) is to vertex i (in
G_B. The similarity matrix can be obtained as the limit of the normalized even
iterates of a linear transformation. In the special case where G_A=G_B=G, the
matrix is square and the (i, j)-th entry is the similarity score between the
vertices i and j of G. We point out that Kleinberg's "hub and authority" method
to identify web-pages relevant to a given query can be viewed as a special case
of our definition in the case where one of the graphs has two vertices and a
unique directed edge between them. In analogy to Kleinberg, we show that our
similarity scores are given by the components of a dominant eigenvector of a
non-negative matrix. Potential applications of our similarity concept are
numerous. We illustrate an application for the automatic extraction of synonyms
in a monolingual dictionary.