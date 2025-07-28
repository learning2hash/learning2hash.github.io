---
layout: publication
title: 'EAGER: Embedding-assisted Entity Resolution For Knowledge Graphs'
authors: Daniel Obraczka, Jonathan Schuchart, Erhard Rahm
conference: Arxiv
year: 2021
bibkey: obraczka2021eager
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.06126'}]
tags: []
short_authors: Daniel Obraczka, Jonathan Schuchart, Erhard Rahm
---
Entity Resolution (ER) is a constitutional part for integrating different
knowledge graphs in order to identify entities referring to the same real-world
object. A promising approach is the use of graph embeddings for ER in order to
determine the similarity of entities based on the similarity of their graph
neighborhood. The similarity computations for such embeddings translates to
calculating the distance between them in the embedding space which is
comparatively simple. However, previous work has shown that the use of graph
embeddings alone is not sufficient to achieve high ER quality. We therefore
propose a more comprehensive ER approach for knowledge graphs called EAGER
(Embedding-Assisted Knowledge Graph Entity Resolution) to flexibly utilize both
the similarity of graph embeddings and attribute values within a supervised
machine learning approach. We evaluate our approach on 23 benchmark datasets
with differently sized and structured knowledge graphs and use hypothesis tests
to ensure statistical significance of our results. Furthermore we compare our
approach with state-of-the-art ER solutions, where our approach yields
competitive results for table-oriented ER problems and shallow knowledge graphs
but much better results for deeper knowledge graphs.