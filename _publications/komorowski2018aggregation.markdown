---
layout: publication
title: Aggregation Of Binary Feature Descriptors For Compact Scene Model Representation
  In Large Scale Structure-from-motion Applications
authors: Jacek Komorowski, Tomasz Trzcinski
conference: Lecture Notes in Computer Science
year: 2018
bibkey: komorowski2018aggregation
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.11062'}]
tags: ["Compact Codes", "Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Jacek Komorowski, Tomasz Trzcinski
---
In this paper we present an efficient method for aggregating binary feature
descriptors to allow compact representation of 3D scene model in incremental
structure-from-motion and SLAM applications. All feature descriptors linked
with one 3D scene point or landmark are represented by a single low-dimensional
real-valued vector called a *prototype*. The method allows significant
reduction of memory required to store and process feature descriptors in
large-scale structure-from-motion applications. An efficient approximate
nearest neighbours search methods suited for real-valued descriptors, such as
FLANN, can be used on the resulting prototypes to speed up matching processed
frames.