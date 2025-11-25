---
layout: publication
title: 'REVEAL: Retrieval-augmented Visual-language Pre-training With Multi-source
  Multimodal Knowledge Memory'
authors: Ziniu Hu, Ahmet Iscen, Chen Sun, Zirui Wang, Kai-Wei Chang, Yizhou Sun, Cordelia
  Schmid, David A. Ross, Alireza Fathi
conference: Arxiv
year: 2022
bibkey: hu2022reveal
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.05221'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Scalability"]
short_authors: Hu et al.
---
In this paper, we propose an end-to-end Retrieval-Augmented Visual Language
Model (REVEAL) that learns to encode world knowledge into a large-scale memory,
and to retrieve from it to answer knowledge-intensive queries. REVEAL consists
of four key components: the memory, the encoder, the retriever and the
generator. The large-scale memory encodes various sources of multimodal world
knowledge (e.g. image-text pairs, question answering pairs, knowledge graph
triplets, etc) via a unified encoder. The retriever finds the most relevant
knowledge entries in the memory, and the generator fuses the retrieved
knowledge with the input query to produce the output. A key novelty in our
approach is that the memory, encoder, retriever and generator are all
pre-trained end-to-end on a massive amount of data. Furthermore, our approach
can use a diverse set of multimodal knowledge sources, which is shown to result
in significant gains. We show that REVEAL achieves state-of-the-art results on
visual question answering and image captioning.