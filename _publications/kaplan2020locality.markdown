---
layout: publication
title: Locality Sensitive Hashing For Set-queries Motivated By Group Recommendations
authors: Kaplan Haim, Tenenbaum Jay
conference: "Arxiv"
year: 2020
bibkey: kaplan2020locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2004.07286"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Locality Sensitive Hashing (LSH) is an effective method to index a set of
points such that we can efficiently find the nearest neighbors of a query
point. We extend this method to our novel Set-query LSH (SLSH), such that it
can find the nearest neighbors of a set of points, given as a query.
  Let \\{ s(x,y) \\} be the similarity between two points \\{ x \\} and \\{ y \\}. We
define a similarity between a set \\{ Q\\} and a point \\{ x \\} by aggregating the
similarities \\{ s(p,x) \\} for all \\{ p\in Q \\}. For example, we can take \\{ s(p,x) \\}
to be the angular similarity between \\{ p \\} and \\{ x \\} (i.e., \\{1-\{\angle
(x,p)\}/\{\pi\}\\}), and aggregate by arithmetic or geometric averaging, or taking
the lowest similarity.
  We develop locality sensitive hash families and data structures for a large
set of such arithmetic and geometric averaging similarities, and analyze their
collision probabilities. We also establish an analogous framework and hash
families for distance functions. Specifically, we give a structure for the
euclidean distance aggregated by either averaging or taking the maximum.
  We leverage SLSH to solve a geometric extension of the approximate near
neighbors problem. In this version, we consider a metric for which the unit
ball is an ellipsoid and its orientation is specified with the query.
  An important application that motivates our work is group recommendation
systems. Such a system embeds movies and users in the same feature space, and
the task of recommending a movie for a group to watch together, translates to a
set-query \\{ Q \\} using an appropriate similarity.
