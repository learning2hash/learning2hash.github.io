---
layout: publication
title: Enhanced Vectors For Top-k Document Retrieval In Question Answering
authors: Mohammed Hammad
conference: Arxiv
year: 2022
bibkey: hammad2022enhanced
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.10584'}]
tags: [Text Retrieval, Efficiency]
short_authors: Mohammed Hammad
---
Modern day applications, especially information retrieval webapps that
involve "search" as their use cases are gradually moving towards "answering"
modules. Conversational chatbots which have been proved to be more engaging to
users, use Question Answering as their core. Since, precise answering is
computationally expensive, several approaches have been developed to prefetch
the most relevant documents/passages from the database that contain the answer.
We propose a different approach that retrieves the evidence documents
efficiently and accurately, making sure that the relevant document for a given
user query is not missed. We do so by assigning each document (or passage in
our case), a unique identifier and using them to create dense vectors which can
be efficiently indexed. More precisely, we use the identifier to predict
randomly sampled context window words of the relevant question corresponding to
the passage along with the words of passage itself. This naturally embeds the
passage identifier into the vector space in such a way that the embedding is
closer to the question without compromising he information content. This
approach enables efficient creation of real-time query vectors in ~4
milliseconds.