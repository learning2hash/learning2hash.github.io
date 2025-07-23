---
layout: publication
title: Pseudo-relevance Feedback For Multiple Representation Dense Retrieval
authors: Wang Xiao, Macdonald Craig, Tonellotto Nicola, Ounis Iadh
conference: Proceedings of the 2021 ACM SIGIR International Conference on Theory of
  Information Retrieval
year: 2021
bibkey: wang2021pseudo
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.11251'}]
tags: ["Evaluation", "Large-Scale Search", "Re-ranking", "SIGIR", "Text Retrieval"]
short_authors: Wang et al.
---
Pseudo-relevance feedback mechanisms, from Rocchio to the relevance models,
have shown the usefulness of expanding and reweighting the users' initial
queries using information occurring in an initial set of retrieved documents,
known as the pseudo-relevant set. Recently, dense retrieval -- through the use
of neural contextual language models such as BERT for analysing the documents'
and queries' contents and computing their relevance scores -- has shown a
promising performance on several information retrieval tasks still relying on
the traditional inverted index for identifying documents relevant to a query.
Two different dense retrieval families have emerged: the use of single embedded
representations for each passage and query (e.g. using BERT's [CLS] token), or
via multiple representations (e.g. using an embedding for each token of the
query and document). In this work, we conduct the first study into the
potential for multiple representation dense retrieval to be enhanced using
pseudo-relevance feedback. In particular, based on the pseudo-relevant set of
documents identified using a first-pass dense retrieval, we extract
representative feedback embeddings (using KMeans clustering) -- while ensuring
that these embeddings discriminate among passages (based on IDF) -- which are
then added to the query representation. These additional feedback embeddings
are shown to both enhance the effectiveness of a reranking as well as an
additional dense retrieval operation. Indeed, experiments on the MSMARCO
passage ranking dataset show that MAP can be improved by upto 26% on the TREC
2019 query set and 10% on the TREC 2020 query set by the application of our
proposed ColBERT-PRF method on a ColBERT dense retrieval approach.