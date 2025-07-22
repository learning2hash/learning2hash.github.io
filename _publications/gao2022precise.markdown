---
layout: publication
title: Precise Zero-Shot Dense Retrieval without Relevance Labels
authors: Gao Luyu, Ma Xueguang, Lin Jimmy, Callan Jamie
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: gao2022precise
citations: 81
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.10496'}]
tags: ["Unsupervised", "Few-Shot-&-Zero-Shot", "Evaluation"]
short_authors: Gao et al.
---
While dense retrieval has been shown effective and efficient across tasks and
languages, it remains difficult to create effective fully zero-shot dense
retrieval systems when no relevance label is available. In this paper, we
recognize the difficulty of zero-shot learning and encoding relevance. Instead,
we propose to pivot through Hypothetical Document Embeddings~(HyDE). Given a
query, HyDE first zero-shot instructs an instruction-following language model
(e.g. InstructGPT) to generate a hypothetical document. The document captures
relevance patterns but is unreal and may contain false details. Then, an
unsupervised contrastively learned encoder~(e.g. Contriever) encodes the
document into an embedding vector. This vector identifies a neighborhood in the
corpus embedding space, where similar real documents are retrieved based on
vector similarity. This second step ground the generated document to the actual
corpus, with the encoder's dense bottleneck filtering out the incorrect
details. Our experiments show that HyDE significantly outperforms the
state-of-the-art unsupervised dense retriever Contriever and shows strong
performance comparable to fine-tuned retrievers, across various tasks (e.g. web
search, QA, fact verification) and languages~(e.g. sw, ko, ja).