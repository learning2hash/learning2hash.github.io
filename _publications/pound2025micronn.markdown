---
layout: publication
title: 'Micronn: An On-device Disk-resident Updatable Vector Database'
authors: Pound Jeffrey, Chabert Floris, Bhushan Arjun, Goswami Ankur, Pacaci Anil,
  Chowdhury Shihabur Rahman
conference: Companion of the 2025 International Conference on Management of Data
year: 2025
bibkey: pound2025micronn
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.05573'}]
tags: ["Efficiency", "Evaluation", "Scalability", "Similarity Search", "Tools & Libraries", "Vector Indexing"]
short_authors: Pound et al.
---
Nearest neighbour search over dense vector collections has important
applications in information retrieval, retrieval augmented generation (RAG),
and content ranking. Performing efficient search over large vector collections
is a well studied problem with many existing approaches and open source
implementations. However, most state-of-the-art systems are generally targeted
towards scenarios using large servers with an abundance of memory, static
vector collections that are not updatable, and nearest neighbour search in
isolation of other search criteria. We present Micro Nearest Neighbour
(MicroNN), an embedded nearest-neighbour vector search engine designed for
scalable similarity search in low-resource environments. MicroNN addresses the
problem of on-device vector search for real-world workloads containing updates
and hybrid search queries that combine nearest neighbour search with structured
attribute filters. In this scenario, memory is highly constrained and
disk-efficient index structures and algorithms are required, as well as support
for continuous inserts and deletes. MicroNN is an embeddable library that can
scale to large vector collections with minimal resources. MicroNN is used in
production and powers a wide range of vector search use-cases on-device.
MicroNN takes less than 7 ms to retrieve the top-100 nearest neighbours with
90% recall on publicly available million-scale vector benchmark while using ~10
MB of memory.