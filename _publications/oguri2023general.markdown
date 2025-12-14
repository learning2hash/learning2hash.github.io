---
layout: publication
title: 'General And Practical Tuning Method For Off-the-shelf Graph-based Index: SISAP
  Indexing Challenge Report By Team Utokyo'
authors: Yutaro Oguri, Yusuke Matsui
conference: Lecture Notes in Computer Science
year: 2023
bibkey: oguri2023general
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.00472'}]
tags: [Evaluation, Graph-based ANN]
short_authors: Yutaro Oguri, Yusuke Matsui
---
Despite the efficacy of graph-based algorithms for Approximate Nearest
Neighbor (ANN) searches, the optimal tuning of such systems remains unclear.
This study introduces a method to tune the performance of off-the-shelf
graph-based indexes, focusing on the dimension of vectors, database size, and
entry points of graph traversal. We utilize a black-box optimization algorithm
to perform integrated tuning to meet the required levels of recall and Queries
Per Second (QPS). We applied our approach to Task A of the SISAP 2023 Indexing
Challenge and got second place in the 10M and 30M tracks. It improves
performance substantially compared to brute force methods. This research offers
a universally applicable tuning method for graph-based indexes, extending
beyond the specific conditions of the competition to broader uses.