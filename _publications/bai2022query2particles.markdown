---
layout: publication
title: 'Query2particles: Knowledge Graph Reasoning With Particle Embeddings'
authors: Jiaxin Bai, Zihao Wang, Hongming Zhang, Yangqiu Song
conference: 'Findings of the Association for Computational Linguistics: NAACL 2022'
year: 2022
bibkey: bai2022query2particles
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.12847'}]
tags: [ACL, NAACL, Evaluation]
short_authors: Bai et al.
---
Answering complex logical queries on incomplete knowledge graphs (KGs) with
missing edges is a fundamental and important task for knowledge graph
reasoning. The query embedding method is proposed to answer these queries by
jointly encoding queries and entities to the same embedding space. Then the
answer entities are selected according to the similarities between the entity
embeddings and the query embedding. As the answers to a complex query are
obtained from a combination of logical operations over sub-queries, the
embeddings of the answer entities may not always follow a uni-modal
distribution in the embedding space. Thus, it is challenging to simultaneously
retrieve a set of diverse answers from the embedding space using a single and
concentrated query representation such as a vector or a hyper-rectangle. To
better cope with queries with diversified answers, we propose Query2Particles
(Q2P), a complex KG query answering method. Q2P encodes each query into
multiple vectors, named particle embeddings. By doing so, the candidate answers
can be retrieved from different areas over the embedding space using the
maximal similarities between the entity embeddings and any of the particle
embeddings. Meanwhile, the corresponding neural logic operations are defined to
support its reasoning over arbitrary first-order logic queries. The experiments
show that Query2Particles achieves state-of-the-art performance on the complex
query answering tasks on FB15k, FB15K-237, and NELL knowledge graphs.