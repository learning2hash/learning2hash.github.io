---
layout: publication
title: Structure And Semantics Preserving Document Representations
authors: Natraj Raman, Sameena Shah, Manuela Veloso
conference: Proceedings of the 45th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2022
bibkey: raman2022structure
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.03720'}]
tags: ["SIGIR", "Text Retrieval"]
short_authors: Natraj Raman, Sameena Shah, Manuela Veloso
---
Retrieving relevant documents from a corpus is typically based on the
semantic similarity between the document content and query text. The inclusion
of structural relationship between documents can benefit the retrieval
mechanism by addressing semantic gaps. However, incorporating these
relationships requires tractable mechanisms that balance structure with
semantics and take advantage of the prevalent pre-train/fine-tune paradigm. We
propose here a holistic approach to learning document representations by
integrating intra-document content with inter-document relations. Our deep
metric learning solution analyzes the complex neighborhood structure in the
relationship network to efficiently sample similar/dissimilar document pairs
and defines a novel quintuplet loss function that simultaneously encourages
document pairs that are semantically relevant to be closer and structurally
unrelated to be far apart in the representation space. Furthermore, the
separation margins between the documents are varied flexibly to encode the
heterogeneity in relationship strengths. The model is fully fine-tunable and
natively supports query projection during inference. We demonstrate that it
outperforms competing methods on multiple datasets for document retrieval
tasks.