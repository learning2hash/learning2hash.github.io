---
layout: publication
title: Unsupervised Person Re-identification Via Multi-label Prediction And Classification
  Based On Graph-structural Insight
authors: Jongmin Yu, Hyeontaek Oh
conference: Arxiv
year: 2021
bibkey: yu2021unsupervised
citations: 0
additional_links: [{name: Code, url: 'https://github.com/uknownpioneer/GSMLP-SMLC.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.08798'}]
tags: ["Unsupervised"]
short_authors: Jongmin Yu, Hyeontaek Oh
---
This paper addresses unsupervised person re-identification (Re-ID) using
multi-label prediction and classification based on graph-structural insight.
Our method extracts features from person images and produces a graph that
consists of the features and a pairwise similarity of them as nodes and edges,
respectively. Based on the graph, the proposed graph structure based
multi-label prediction (GSMLP) method predicts multi-labels by considering the
pairwise similarity and the adjacency node distribution of each node. The
multi-labels created by GSMLP are applied to the proposed selective multi-label
classification (SMLC) loss. SMLC integrates a hard-sample mining scheme and a
multi-label classification. The proposed GSMLP and SMLC boost the performance
of unsupervised person Re-ID without any pre-labelled dataset. Experimental
results justify the superiority of the proposed method in unsupervised person
Re-ID by producing state-of-the-art performance. The source code for this paper
is publicly available on 'https://github.com/uknownpioneer/GSMLP-SMLC.git'.