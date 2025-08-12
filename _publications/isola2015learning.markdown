---
layout: publication
title: Learning Visual Groups From Co-occurrences In Space And Time
authors: Phillip Isola, Daniel Zoran, Dilip Krishnan, Edward H. Adelson
conference: Arxiv
year: 2015
bibkey: isola2015learning
citations: 93
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.06811'}]
tags: []
short_authors: Isola et al.
---
We propose a self-supervised framework that learns to group visual entities
based on their rate of co-occurrence in space and time. To model statistical
dependencies between the entities, we set up a simple binary classification
problem in which the goal is to predict if two visual primitives occur in the
same spatial or temporal context. We apply this framework to three domains:
learning patch affinities from spatial adjacency in images, learning frame
affinities from temporal adjacency in videos, and learning photo affinities
from geospatial proximity in image collections. We demonstrate that in each
case the learned affinities uncover meaningful semantic groupings. From patch
affinities we generate object proposals that are competitive with
state-of-the-art supervised methods. From frame affinities we generate movie
scene segmentations that correlate well with DVD chapter structure. Finally,
from geospatial affinities we learn groups that relate well to semantic place
categories.