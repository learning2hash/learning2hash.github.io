---
layout: publication
title: 'TBIN: Modeling Long Textual Behavior Data For CTR Prediction'
authors: Shuwei Chen, Xiang Li, Jian Dong, Jin Zhang, Yongkang Wang, Xingxing Wang
conference: Arxiv
year: 2023
bibkey: chen2023tbin
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.08483'}]
tags: ["Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Chen et al.
---
Click-through rate (CTR) prediction plays a pivotal role in the success of
recommendations. Inspired by the recent thriving of language models (LMs), a
surge of works improve prediction by organizing user behavior data in a
\textbf\{textual\} format and using LMs to understand user interest at a semantic
level. While promising, these works have to truncate the textual data to reduce
the quadratic computational overhead of self-attention in LMs. However, it has
been studied that long user behavior data can significantly benefit CTR
prediction. In addition, these works typically condense user diverse interests
into a single feature vector, which hinders the expressive capability of the
model. In this paper, we propose a \textbf\{T\}extual \textbf\{B\}ehavior-based
\textbf\{I\}nterest Chunking \textbf\{N\}etwork (TBIN), which tackles the above
limitations by combining an efficient locality-sensitive hashing algorithm and
a shifted chunk-based self-attention. The resulting user diverse interests are
dynamically activated, producing user interest representation towards the
target item. Finally, the results of both offline and online experiments on
real-world food recommendation platform demonstrate the effectiveness of TBIN.