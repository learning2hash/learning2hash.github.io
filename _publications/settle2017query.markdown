---
layout: publication
title: Query-by-example Search With Discriminative Neural Acoustic Word Embeddings
authors: Settle et al.
conference: Interspeech 2017
year: 2017
bibkey: settle2017query
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.03818'}]
tags: [Efficiency And Optimization, INTERSPEECH, Evaluation]
---
Query-by-example search often uses dynamic time warping (DTW) for comparing
queries and proposed matching segments. Recent work has shown that comparing
speech segments by representing them as fixed-dimensional vectors --- acoustic
word embeddings --- and measuring their vector distance (e.g., cosine distance)
can discriminate between words more accurately than DTW-based approaches. We
consider an approach to query-by-example search that embeds both the query and
database segments according to a neural model, followed by nearest-neighbor
search to find the matching segments. Earlier work on embedding-based
query-by-example, using template-based acoustic word embeddings, achieved
competitive performance. We find that our embeddings, based on recurrent neural
networks trained to optimize word discrimination, achieve substantial
improvements in performance and run-time efficiency over the previous
approaches.