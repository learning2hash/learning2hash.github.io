---
layout: publication
title: Using Images To Create A Hierarchical Grid Spatial Index
authors: Lukasz A. MacHowski, Tshilidzi Marwala
conference: 2006 IEEE International Conference on Systems, Man and Cybernetics
year: 2006
bibkey: machowski2006using
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0705.0204'}]
tags: ["Image Retrieval", "Vector Indexing"]
short_authors: Lukasz A. MacHowski, Tshilidzi Marwala
---
This paper presents a hybrid approach to spatial indexing of two dimensional
data. It sheds new light on the age old problem by thinking of the traditional
algorithms as working with images. Inspiration is drawn from an analogous
situation that is found in machine and human vision. Image processing
techniques are used to assist in the spatial indexing of the data. A fixed grid
approach is used and bins with too many records are sub-divided hierarchically.
Search queries are pre-computed for bins that do not contain any data records.
This has the effect of dividing the search space up into non rectangular
regions which are based on the spatial properties of the data. The bucketing
quad tree can be considered as an image with a resolution of two by two for
each layer. The results show that this method performs better than the quad
tree if there are more divisions per layer. This confirms our suspicions that
the algorithm works better if it gets to look at the data with higher
resolution images. An elegant class structure is developed where the
implementation of concrete spatial indexes for a particular data type merely
relies on rendering the data onto an image.