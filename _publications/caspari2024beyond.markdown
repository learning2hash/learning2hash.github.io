---
layout: publication
title: 'Beyond Benchmarks: Evaluating Embedding Model Similarity For Retrieval Augmented
  Generation Systems'
authors: Laura Caspari, Kanishka Ghosh Dastidar, Saber Zerhoudi, Jelena Mitrovic,
  Michael Granitzer
conference: Arxiv
year: 2024
bibkey: caspari2024beyond
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.08275'}]
tags: [Datasets, Evaluation]
short_authors: Caspari et al.
---
The choice of embedding model is a crucial step in the design of Retrieval
Augmented Generation (RAG) systems. Given the sheer volume of available
options, identifying clusters of similar models streamlines this model
selection process. Relying solely on benchmark performance scores only allows
for a weak assessment of model similarity. Thus, in this study, we evaluate the
similarity of embedding models within the context of RAG systems. Our
assessment is two-fold: We use Centered Kernel Alignment to compare embeddings
on a pair-wise level. Additionally, as it is especially pertinent to RAG
systems, we evaluate the similarity of retrieval results between these models
using Jaccard and rank similarity. We compare different families of embedding
models, including proprietary ones, across five datasets from the popular
Benchmark Information Retrieval (BEIR). Through our experiments we identify
clusters of models corresponding to model families, but interestingly, also
some inter-family clusters. Furthermore, our analysis of top-k retrieval
similarity reveals high-variance at low k values. We also identify possible
open-source alternatives to proprietary models, with Mistral exhibiting the
highest similarity to OpenAI models.