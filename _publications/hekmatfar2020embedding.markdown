---
layout: publication
title: Embedding Ranking-Oriented Recommender System Graphs
authors: Hekmatfar Taher, Haratizadeh Saman, Goliaei Sama
conference: Expert Systems with Applications
year: 2021
bibkey: hekmatfar2020embedding
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.16173'}]
tags: ["Tools-&-Libraries", "Graph-Based-ANN", "Datasets", "Recommender-Systems", "Evaluation"]
short_authors: Hekmatfar Taher, Haratizadeh Saman, Goliaei Sama
---
Graph-based recommender systems (GRSs) analyze the structural information in
the graphical representation of data to make better recommendations, especially
when the direct user-item relation data is sparse. Ranking-oriented GRSs that
form a major class of recommendation systems, mostly use the graphical
representation of preference (or rank) data for measuring node similarities,
from which they can infer a recommendation list using a neighborhood-based
mechanism. In this paper, we propose PGRec, a novel graph-based
ranking-oriented recommendation framework. PGRec models the preferences of the
users over items, by a novel graph structure called PrefGraph. This graph is
then exploited by an improved embedding approach, taking advantage of both
factorization and deep learning methods, to extract vectors representing users,
items, and preferences. The resulting embedding are then used for predicting
users' unknown pairwise preferences from which the final recommendation lists
are inferred. We have evaluated the performance of the proposed method against
the state of the art model-based and neighborhood-based recommendation methods,
and our experiments show that PGRec outperforms the baseline algorithms up to
3.2% in terms of NDCG@10 in different MovieLens datasets.