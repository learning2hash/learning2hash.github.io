---
layout: publication
title: 'Zoom: Ssd-based Vector Search For Optimizing Accuracy, Latency And Memory'
authors: Zhang Minjia, He Yuxiong
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2018
bibkey: zhang2018zoom
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.04067'}]
---
With the advancement of machine learning and deep learning, vector search
becomes instrumental to many information retrieval systems, to search and find
best matches to user queries based on their semantic similarities.These online
services require the search architecture to be both effective with high
accuracy and efficient with low latency and memory footprint, which existing
work fails to offer. We develop, Zoom, a new vector search solution that
collaboratively optimizes accuracy, latency and memory based on a multiview
approach. (1) A "preview" step generates a small set of good candidates,
leveraging compressed vectors in memory for reduced footprint and fast lookup.
(2) A "fullview" step on SSDs reranks those candidates with their full-length
vector, striking high accuracy. Our evaluation shows that, Zoom achieves an
order of magnitude improvements on efficiency while attaining equal or higher
accuracy, comparing with the state-of-the-art.