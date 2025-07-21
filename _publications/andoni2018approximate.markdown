---
layout: publication
title: Approximate Nearest Neighbor Search in High Dimensions
authors: Andoni Alexandr, Indyk Piotr, Razenshteyn Ilya
conference: 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition
year: 2010
bibkey: andoni2018approximate
citations: 109
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.09823'}]
tags: ["CVPR"]
---
The nearest neighbor problem is defined as follows: Given a set \\(P\\) of \\(n\\)
points in some metric space \\((X,D)\\), build a data structure that, given any
point \\(q\\), returns a point in \\(P\\) that is closest to \\(q\\) (its "nearest
neighbor" in \\(P\\)). The data structure stores additional information about the
set \\(P\\), which is then used to find the nearest neighbor without computing all
distances between \\(q\\) and \\(P\\). The problem has a wide range of applications in
machine learning, computer vision, databases and other fields.
  To reduce the time needed to find nearest neighbors and the amount of memory
used by the data structure, one can formulate the \{\em approximate\} nearest
neighbor problem, where the the goal is to return any point \\(p' \in P\\) such
that the distance from \\(q\\) to \\(p'\\) is at most \\(c \cdot \min_\{p \in P\} D(q,p)\\),
for some \\(c \geq 1\\). Over the last two decades, many efficient solutions to
this problem were developed. In this article we survey these developments, as
well as their connections to questions in geometric functional analysis and
combinatorial geometry.