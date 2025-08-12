---
layout: publication
title: Spherical Indexing For Neighborhood Queries
authors: Nicolas Brodu
conference: Arxiv
year: 2006
bibkey: brodu2006spherical
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0608108'}]
tags: ["Similarity Search", "Vector Indexing"]
short_authors: Nicolas Brodu
---
This is an algorithm for finding neighbors when the objects can freely move
and have no predefined position. The query consists in finding neighbors for a
center location and a given radius. Space is discretized in cubic cells. This
algorithm introduces a direct spherical indexing that gives the list of all
cells making up the query sphere, for any radius and any center location. It
can additionally take in account both cyclic and non-cyclic regions of
interest. Finding only the K nearest neighbors naturally benefits from the
spherical indexing by minimally running through the sphere from center to edge,
and reducing the maximum distance when K neighbors have been found.