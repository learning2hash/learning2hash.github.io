---
layout: publication
title: Structured Query-based Image Retrieval Using Scene Graphs
authors: Brigit Schroeder, Subarna Tripathi
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: schroeder2020structured
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.06653'}]
tags: ["CVPR", "Datasets", "Evaluation", "Image Retrieval"]
short_authors: Brigit Schroeder, Subarna Tripathi
---
A structured query can capture the complexity of object interactions (e.g.
'woman rides motorcycle') unlike single objects (e.g. 'woman' or 'motorcycle').
Retrieval using structured queries therefore is much more useful than single
object retrieval, but a much more challenging problem. In this paper we present
a method which uses scene graph embeddings as the basis for an approach to
image retrieval. We examine how visual relationships, derived from scene
graphs, can be used as structured queries. The visual relationships are
directed subgraphs of the scene graph with a subject and object as nodes
connected by a predicate relationship. Notably, we are able to achieve high
recall even on low to medium frequency objects found in the long-tailed
COCO-Stuff dataset, and find that adding a visual relationship-inspired loss
boosts our recall by 10% in the best case.