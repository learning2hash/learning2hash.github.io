---
layout: publication
title: Graph-based Clustering For Detecting Semantic Change Across Time And Languages
authors: Xianghe Ma, Michael Strube, Wei Zhao
conference: 'Proceedings of the 18th Conference of the European Chapter of the Association
  for Computational Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: ma2024graph
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.01025'}]
tags: ["Eacl"]
short_authors: Xianghe Ma, Michael Strube, Wei Zhao
---
Despite the predominance of contextualized embeddings in NLP, approaches to
detect semantic change relying on these embeddings and clustering methods
underperform simpler counterparts based on static word embeddings. This stems
from the poor quality of the clustering methods to produce sense clusters --
which struggle to capture word senses, especially those with low frequency.
This issue hinders the next step in examining how changes in word senses in one
language influence another. To address this issue, we propose a graph-based
clustering approach to capture nuanced changes in both high- and low-frequency
word senses across time and languages, including the acquisition and loss of
these senses over time. Our experimental results show that our approach
substantially surpasses previous approaches in the SemEval2020 binary
classification task across four languages. Moreover, we showcase the ability of
our approach as a versatile visualization tool to detect semantic changes in
both intra-language and inter-language setups. We make our code and data
publicly available.