---
layout: publication
title: Graph Based Temporal Aggregation For Video Retrieval
authors: Arvind Srinivasan, Aprameya Bharadwaj, Aveek Saha, Subramanyam Natarajan
conference: Arxiv
year: 2020
bibkey: srinivasan2020graph
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.02426'}]
tags: [Video Retrieval, Graph-based ANN, Scalability, Datasets]
short_authors: Srinivasan et al.
---
Large scale video retrieval is a field of study with a lot of ongoing
research. Most of the work in the field is on video retrieval through text
queries using techniques such as VSE++. However, there is little research done
on video retrieval through image queries, and the work that has been done in
this field either uses image queries from within the video dataset or iterates
through videos frame by frame. These approaches are not generalized for queries
from outside the dataset and do not scale well for large video datasets. To
overcome these issues, we propose a new approach for video retrieval through
image queries where an undirected graph is constructed from the combined set of
frames from all videos to be searched. The node features of this graph are used
in the task of video retrieval. Experimentation is done on the MSR-VTT dataset
by using query images from outside the dataset. To evaluate this novel approach
P@5, P@10 and P@20 metrics are calculated. Two different ResNet models namely,
ResNet-152 and ResNet-50 are used in this study.