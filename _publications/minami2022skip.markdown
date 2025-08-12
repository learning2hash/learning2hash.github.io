---
layout: publication
title: 'Skip Vectors For RDF Data: Extraction Based On The Complexity Of Feature Patterns'
authors: Yota Minami, Ken Kaneiwa
conference: Arxiv
year: 2022
bibkey: minami2022skip
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.01996'}]
tags: []
short_authors: Yota Minami, Ken Kaneiwa
---
The Resource Description Framework (RDF) is a framework for describing
metadata, such as attributes and relationships of resources on the Web. Machine
learning tasks for RDF graphs adopt three methods: (i) support vector machines
(SVMs) with RDF graph kernels, (ii) RDF graph embeddings, and (iii) relational
graph convolutional networks. In this paper, we propose a novel feature vector
(called a Skip vector) that represents some features of each resource in an RDF
graph by extracting various combinations of neighboring edges and nodes. In
order to make the Skip vector low-dimensional, we select important features for
classification tasks based on the information gain ratio of each feature. The
classification tasks can be performed by applying the low-dimensional Skip
vector of each resource to conventional machine learning algorithms, such as
SVMs, the k-nearest neighbors method, neural networks, random forests, and
AdaBoost. In our evaluation experiments with RDF data, such as Wikidata,
DBpedia, and YAGO, we compare our method with RDF graph kernels in an SVM. We
also compare our method with the two approaches: RDF graph embeddings such as
RDF2vec and relational graph convolutional networks on the AIFB, MUTAG, BGS,
and AM benchmarks.