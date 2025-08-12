---
layout: publication
title: 'Hash-based Ray Path Prediction: Skipping BVH Traversal Computation By Exploiting
  Ray Locality'
authors: Francois Demoullin, Ayub Gubran, Tor Aamodt
conference: Arxiv
year: 2019
bibkey: demoullin2019hash
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.01304'}]
tags: []
short_authors: Francois Demoullin, Ayub Gubran, Tor Aamodt
---
State-of-the-art ray tracing techniques operate on hierarchical acceleration
structures such as BVH trees which wrap objects in a scene into bounding
volumes of decreasing sizes. Acceleration structures reduce the amount of
ray-scene intersections that a ray has to perform to find the intersecting
object. However, we observe a large amount of redundancy when rays are
traversing these acceleration structures. While modern acceleration structures
explore the spatial organization of the scene, they neglect similarities
between rays that traverse the structures and thereby cause redundant
traversals. This paper provides a limit study of a new promising technique,
Hash-Based Ray Path Prediction (HRPP), which exploits the similarity between
rays to predict leaf nodes to avoid redundant acceleration structure
traversals. Our data shows that acceleration structure traversal consumes a
significant proportion of the ray tracing rendering time regardless of the
platform or the target image quality. Our study quantifies unused ray locality
and evaluates the theoretical potential for improved ray traversal performance
for both coherent and seemingly incoherent rays. We show that HRPP is able to
skip, on average, 40% of all hit-all traversal computations.