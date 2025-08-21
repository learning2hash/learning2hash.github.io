---
layout: publication
title: A Triangle Inequality For Cosine Similarity
authors: Erich Schubert
conference: Lecture Notes in Computer Science
year: 2021
bibkey: schubert2021a
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.04071'}]
tags: ["Distance Metric Learning", "Hashing Methods", "Similarity Search", "Tree Based ANN"]
short_authors: Erich Schubert
---
Similarity search is a fundamental problem for many data analysis techniques.
Many efficient search techniques rely on the triangle inequality of metrics,
which allows pruning parts of the search space based on transitive bounds on
distances. Recently, Cosine similarity has become a popular alternative choice
to the standard Euclidean metric, in particular in the context of textual data
and neural network embeddings. Unfortunately, Cosine similarity is not metric
and does not satisfy the standard triangle inequality. Instead, many search
techniques for Cosine rely on approximation techniques such as locality
sensitive hashing. In this paper, we derive a triangle inequality for Cosine
similarity that is suitable for efficient similarity search with many standard
search structures (such as the VP-tree, Cover-tree, and M-tree); show that this
bound is tight and discuss fast approximations for it. We hope that this spurs
new research on accelerating exact similarity search for cosine similarity, and
possible other similarity measures beyond the existing work for distance
metrics.