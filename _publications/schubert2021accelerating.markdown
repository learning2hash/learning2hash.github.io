---
layout: publication
title: Accelerating Spherical K-means
authors: Erich Schubert, Andreas Lang, Gloria Feher
conference: Lecture Notes in Computer Science
year: 2021
bibkey: schubert2021accelerating
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.04074'}]
tags: ["Efficiency"]
short_authors: Erich Schubert, Andreas Lang, Gloria Feher
---
Spherical k-means is a widely used clustering algorithm for sparse and
high-dimensional data such as document vectors. While several improvements and
accelerations have been introduced for the original k-means algorithm, not all
easily translate to the spherical variant: Many acceleration techniques, such
as the algorithms of Elkan and Hamerly, rely on the triangle inequality of
Euclidean distances. However, spherical k-means uses Cosine similarities
instead of distances for computational efficiency. In this paper, we
incorporate the Elkan and Hamerly accelerations to the spherical k-means
algorithm working directly with the Cosines instead of Euclidean distances to
obtain a substantial speedup and evaluate these spherical accelerations on real
data.