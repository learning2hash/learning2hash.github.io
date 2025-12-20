---
layout: publication
title: Improving Low-resource Cross-lingual Document Retrieval By Reranking With Deep
  Bilingual Representations
authors: Rui Zhang, Caitlin Westerfield, Sungrok Shim, Garrett Bingham, Alexander
  Fabbri, Neha Verma, William Hu, Dragomir Radev
conference: Proceedings of the 57th Annual Meeting of the Association for Computational
  Linguistics
year: 2019
bibkey: zhang2019improving
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.03492'}]
tags: ["Datasets", "Evaluation", "Hybrid ANN Methods", "Re-Ranking", "Text Retrieval"]
short_authors: Zhang et al.
---
In this paper, we propose to boost low-resource cross-lingual document
retrieval performance with deep bilingual query-document representations. We
match queries and documents in both source and target languages with four
components, each of which is implemented as a term interaction-based deep
neural network with cross-lingual word embeddings as input. By including query
likelihood scores as extra features, our model effectively learns to rerank the
retrieved documents by using a small number of relevance labels for
low-resource language pairs. Due to the shared cross-lingual word embedding
space, the model can also be directly applied to another language pair without
any training label. Experimental results on the MATERIAL dataset show that our
model outperforms the competitive translation-based baselines on
English-Swahili, English-Tagalog, and English-Somali cross-lingual information
retrieval tasks.