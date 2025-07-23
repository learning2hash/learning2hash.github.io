---
layout: publication
title: A Fast Partial Video Copy Detection Using KNN And Global Feature Database
authors: Tan Weijun, Guo Hongwei, Liu Rushuai
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2022
bibkey: tan2021fast
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01713'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Similarity Search", "Tools & Libraries", "Video Retrieval"]
short_authors: Tan Weijun, Guo Hongwei, Liu Rushuai
---
We propose a fast partial video copy detection framework in this paper. In
this framework all frame features of the reference videos are organized in a
KNN searchable database. Instead of scanning all reference videos, the query
video segment does a fast KNN search in the global feature database. The
returned results are used to generate a short list of candidate videos. A
modified temporal network is then used to localize the copy segment in the
candidate videos. We evaluate different choice of CNN features on the VCDB
dataset. Our benchmark F1 score exceeds the state of the art by a big margin.