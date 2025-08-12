---
layout: publication
title: Streaming K-means Clustering With Fast Queries
authors: Yu Zhang, Kanat Tangwongsan, Srikanta Tirthapura
conference: 2017 IEEE 33rd International Conference on Data Engineering (ICDE)
year: 2017
bibkey: zhang2017streaming
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.03826'}]
tags: ["Efficiency"]
short_authors: Yu Zhang, Kanat Tangwongsan, Srikanta Tirthapura
---
We present methods for k-means clustering on a stream with a focus on
providing fast responses to clustering queries. Compared to the current
state-of-the-art, our methods provide substantial improvement in the query time
for cluster centers while retaining the desirable properties of provably small
approximation error and low space usage. Our algorithms rely on a novel idea of
"coreset caching" that systematically reuses coresets (summaries of data)
computed for recent queries in answering the current clustering query. We
present both theoretical analysis and detailed experiments demonstrating their
correctness and efficiency