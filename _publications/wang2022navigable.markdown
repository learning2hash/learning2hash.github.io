---
layout: publication
title: Navigable Proximity Graph-driven Native Hybrid Queries With Structured And
  Unstructured Constraints
authors: Mengzhao Wang, Lingwei Lv, Xiaoliang Xu, Yuxiang Wang, Qiang Yue, Jiongkang
  Ni
conference: Arxiv
year: 2022
bibkey: wang2022navigable
citations: 4
additional_links: [{name: Code, url: 'https://github.com/AshenOn3/NHQ'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.13601'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Graph Based ANN", "Similarity Search"]
short_authors: Wang et al.
---
As research interest surges, vector similarity search is applied in multiple
fields, including data mining, computer vision, and information retrieval.
\{Given a set of objects (e.g., a set of images) and a query object, we can
easily transform each object into a feature vector and apply the vector
similarity search to retrieve the most similar objects. However, the original
vector similarity search cannot well support \textit\{hybrid queries\}, where
users not only input unstructured query constraint (i.e., the feature vector of
query object) but also structured query constraint (i.e., the desired
attributes of interest). Hybrid query processing aims at identifying these
objects with similar feature vectors to query object and satisfying the given
attribute constraints. Recent efforts have attempted to answer a hybrid query
by performing attribute filtering and vector similarity search separately and
then merging the results later, which limits efficiency and accuracy because
they are not purpose-built for hybrid queries.\} In this paper, we propose a
native hybrid query (NHQ) framework based on proximity graph (PG), which
provides the specialized \textit\{composite index and joint pruning\} modules for
hybrid queries. We easily deploy existing various PGs on this framework to
process hybrid queries efficiently. Moreover, we present two novel navigable
PGs (NPGs) with optimized edge selection and routing strategies, which obtain
better overall performance than existing PGs. After that, we deploy the
proposed NPGs in NHQ to form two hybrid query methods, which significantly
outperform the state-of-the-art competitors on all experimental datasets
(10\(\times\) faster under the same \textit\{Recall\}), including eight public and
one in-house real-world datasets. Our code and datasets have been released at
https://github.com/AshenOn3/NHQ.