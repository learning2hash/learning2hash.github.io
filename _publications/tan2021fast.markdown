---
layout: publication
title: A Fast Partial Video Copy Detection Using KNN And Global Feature Database
authors: Weijun Tan, Hongwei Guo, Rushuai Liu
conference: IEEE WACV 2022
year: 2021
citations: 13
bibkey: tan2021fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01713'}]
tags: [ANN Search, Evaluation Metrics, Applications]
---
We propose a fast partial video copy detection framework in this paper. In
this framework all frame features of the reference videos are organized in a
KNN searchable database. Instead of scanning all reference videos, the query
video segment does a fast KNN search in the global feature database. The
returned results are used to generate a short list of candidate videos. A
modified temporal network is then used to localize the copy segment in the
candidate videos. We evaluate different choice of CNN features on the VCDB
dataset. Our benchmark F1 score exceeds the state of the art by a big margin.