---
layout: publication
title: 'Incdsi: Incrementally Updatable Document Retrieval'
authors: Varsha Kishore, Chao Wan, Justin Lovelace, Yoav Artzi, Kilian Q. Weinberger
conference: Arxiv
year: 2023
bibkey: kishore2023incdsi
citations: 0
additional_links: [{name: Code, url: 'https://github.com/varshakishore/IncDSI'}, {
    name: Paper, url: 'https://arxiv.org/abs/2307.10323'}]
tags: ["Efficiency", "Text Retrieval"]
short_authors: Kishore et al.
---
Differentiable Search Index is a recently proposed paradigm for document
retrieval, that encodes information about a corpus of documents within the
parameters of a neural network and directly maps queries to corresponding
documents. These models have achieved state-of-the-art performances for
document retrieval across many benchmarks. These kinds of models have a
significant limitation: it is not easy to add new documents after a model is
trained. We propose IncDSI, a method to add documents in real time (about
20-50ms per document), without retraining the model on the entire dataset (or
even parts thereof). Instead we formulate the addition of documents as a
constrained optimization problem that makes minimal changes to the network
parameters. Although orders of magnitude faster, our approach is competitive
with re-training the model on the whole dataset and enables the development of
document retrieval systems that can be updated with new information in
real-time. Our code for IncDSI is available at
https://github.com/varshakishore/IncDSI.