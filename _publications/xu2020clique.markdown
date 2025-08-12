---
layout: publication
title: 'Clique: Spatiotemporal Object Re-identification At The City Scale'
authors: Tiantu Xu, Kaiwen Shen, Yang Fu, Humphrey Shi, Felix Xiaozhu Lin
conference: Arxiv
year: 2020
bibkey: xu2020clique
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.09329'}]
tags: ["Image Retrieval"]
short_authors: Xu et al.
---
Object re-identification (ReID) is a key application of city-scale cameras.
While classic ReID tasks are often considered as image retrieval, we treat them
as spatiotemporal queries for locations and times in which the target object
appeared. Spatiotemporal reID is challenged by the accuracy limitation in
computer vision algorithms and the colossal videos from city cameras. We
present Clique, a practical ReID engine that builds upon two new techniques:
(1) Clique assesses target occurrences by clustering fuzzy object features
extracted by ReID algorithms, with each cluster representing the general
impression of a distinct object to be matched against the input; (2) to search
in videos, Clique samples cameras to maximize the spatiotemporal coverage and
incrementally adds cameras for processing on demand. Through evaluation on 25
hours of videos from 25 cameras, Clique reached a high accuracy of 0.87 (recall
at 5) across 70 queries and runs at 830x of video realtime in achieving high
accuracy.