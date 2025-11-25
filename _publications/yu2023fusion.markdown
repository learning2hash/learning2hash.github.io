---
layout: publication
title: 'Fusion-in-t5: Unifying Document Ranking Signals For Improved Information Retrieval'
authors: Shi Yu, Chenghao Fan, Chenyan Xiong, David Jin, Zhiyuan Liu, Zhenghao Liu
conference: Arxiv
year: 2023
bibkey: yu2023fusion
citations: 2
additional_links: [{name: Code, url: 'https://github.com/OpenMatch/FiT5'}, {name: Paper,
    url: 'https://arxiv.org/abs/2305.14685'}]
tags: ["Re-Ranking", "Text Retrieval"]
short_authors: Yu et al.
---
Common document ranking pipelines in search systems are cascade systems that
involve multiple ranking layers to integrate different information
step-by-step. In this paper, we propose a novel re-ranker Fusion-in-T5 (FiT5),
which integrates text matching information, ranking features, and global
document information into one single unified model via templated-based input
and global attention. Experiments on passage ranking benchmarks MS MARCO and
TREC DL show that FiT5, as one single model, significantly improves ranking
performance over complex cascade pipelines. Analysis finds that through
attention fusion, FiT5 jointly utilizes various forms of ranking information
via gradually attending to related documents and ranking features, and improves
the detection of subtle nuances. Our code is open-sourced at
https://github.com/OpenMatch/FiT5.