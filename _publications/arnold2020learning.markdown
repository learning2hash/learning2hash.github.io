---
layout: publication
title: Learning Contextualized Document Representations For Healthcare Answer Retrieval
authors: "Sebastian Arnold, Betty van Aken, Paul Grundmann, Felix A. Gers, Alexander\
  \ L\xF6ser"
conference: Proceedings of The Web Conference 2020
year: 2020
bibkey: arnold2020learning
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00835'}]
tags: [Self-Supervised, Supervised, Tools & Libraries]
short_authors: Arnold et al.
---
We present Contextual Discourse Vectors (CDV), a distributed document
representation for efficient answer retrieval from long healthcare documents.
Our approach is based on structured query tuples of entities and aspects from
free text and medical taxonomies. Our model leverages a dual encoder
architecture with hierarchical LSTM layers and multi-task training to encode
the position of clinical entities and aspects alongside the document discourse.
We use our continuous representations to resolve queries with short latency
using approximate nearest neighbor search on sentence level. We apply the CDV
model for retrieving coherent answer passages from nine English public health
resources from the Web, addressing both patients and medical professionals.
Because there is no end-to-end training data available for all application
scenarios, we train our model with self-supervised data from Wikipedia. We show
that our generalized model significantly outperforms several state-of-the-art
baselines for healthcare passage ranking and is able to adapt to heterogeneous
domains without additional fine-tuning.