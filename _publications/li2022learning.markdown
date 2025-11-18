---
layout: publication
title: Learning Diverse Document Representations With Deep Query Interactions For
  Dense Retrieval
authors: Zehan Li, Nan Yang, Liang Wang, Furu Wei
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: li2022learning
citations: 78
additional_links: [{name: Code, url: 'https://github.com/jordane95/dual-cross-encoder'},
  {name: Paper, url: 'https://arxiv.org/abs/2208.04232'}]
tags: ["Efficiency", "ICASSP"]
short_authors: Li et al.
---
In this paper, we propose a new dense retrieval model which learns diverse
document representations with deep query interactions. Our model encodes each
document with a set of generated pseudo-queries to get query-informed,
multi-view document representations. It not only enjoys high inference
efficiency like the vanilla dual-encoder models, but also enables deep
query-document interactions in document encoding and provides multi-faceted
representations to better match different queries. Experiments on several
benchmarks demonstrate the effectiveness of the proposed method, out-performing
strong dual encoder baselines.The code is available at
\url\{https://github.com/jordane95/dual-cross-encoder