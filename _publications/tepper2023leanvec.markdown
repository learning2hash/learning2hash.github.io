---
layout: publication
title: 'Leanvec: Searching Vectors Faster By Making Them Fit'
authors: Mariano Tepper, Ishwar Singh Bhati, Cecilia Aguerrebere, Mark Hildebrand,
  Ted Willke
conference: Arxiv
year: 2023
bibkey: tepper2023leanvec
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.16335'}]
tags: ["Multimodal Retrieval", "Neural Hashing", "Quantization", "Similarity Search", "Tools & Libraries"]
short_authors: Tepper et al.
---
Modern deep learning models have the ability to generate high-dimensional
vectors whose similarity reflects semantic resemblance. Thus, similarity
search, i.e., the operation of retrieving those vectors in a large collection
that are similar to a given query, has become a critical component of a wide
range of applications that demand highly accurate and timely answers. In this
setting, the high vector dimensionality puts similarity search systems under
compute and memory pressure, leading to subpar performance. Additionally,
cross-modal retrieval tasks have become increasingly common, e.g., where a user
inputs a text query to find the most relevant images for that query. However,
these queries often have different distributions than the database embeddings,
making it challenging to achieve high accuracy. In this work, we present
LeanVec, a framework that combines linear dimensionality reduction with vector
quantization to accelerate similarity search on high-dimensional vectors while
maintaining accuracy. We present LeanVec variants for in-distribution (ID) and
out-of-distribution (OOD) queries. LeanVec-ID yields accuracies on par with
those from recently introduced deep learning alternatives whose computational
overhead precludes their usage in practice. LeanVec-OOD uses two novel
techniques for dimensionality reduction that consider the query and database
distributions to simultaneously boost the accuracy and the performance of the
framework even further (even presenting competitive results when the query and
database distributions match). All in all, our extensive and varied
experimental results show that LeanVec produces state-of-the-art results, with
up to 3.7x improvement in search throughput and up to 4.9x faster index build
time over the state of the art.