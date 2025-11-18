---
layout: publication
title: 'Spagbol: Spatial-graph-based Orientated Localisation'
authors: Tavis Shore, Oscar Mendez, Simon Hadfield
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: shore2024spagbol
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.15514'}]
tags: ["Datasets", "Graph Based ANN"]
short_authors: Tavis Shore, Oscar Mendez, Simon Hadfield
---
Cross-View Geo-Localisation within urban regions is challenging in part due
to the lack of geo-spatial structuring within current datasets and techniques.
We propose utilising graph representations to model sequences of local
observations and the connectivity of the target location. Modelling as a graph
enables generating previously unseen sequences by sampling with new parameter
configurations. To leverage this newly available information, we propose a
GNN-based architecture, producing spatially strong embeddings and improving
discriminability over isolated image embeddings. We outline SpaGBOL,
introducing three novel contributions. 1) The first graph-structured dataset
for Cross-View Geo-Localisation, containing multiple streetview images per node
to improve generalisation. 2) Introducing GNNs to the problem, we develop the
first system that exploits the correlation between node proximity and feature
similarity. 3) Leveraging the unique properties of the graph representation -
we demonstrate a novel retrieval filtering approach based on neighbourhood
bearings. SpaGBOL achieves state-of-the-art accuracies on the unseen test graph
- with relative Top-1 retrieval improvements on previous techniques of 11%, and
50% when filtering with Bearing Vector Matching on the SpaGBOL dataset.