---
layout: publication
title: Unsupervised Document Expansion For Information Retrieval With Stochastic Text
  Generation
authors: Soyeong Jeong, Jinheon Baek, Chaehun Park, Jong C. Park
conference: Proceedings of the Second Workshop on Scholarly Document Processing
year: 2021
bibkey: jeong2021unsupervised
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.00666'}]
tags: [Evaluation, Supervised, Datasets, Tools & Libraries, Unsupervised]
short_authors: Jeong et al.
---
One of the challenges in information retrieval (IR) is the vocabulary
mismatch problem, which happens when the terms between queries and documents
are lexically different but semantically similar. While recent work has
proposed to expand the queries or documents by enriching their representations
with additional relevant terms to address this challenge, they usually require
a large volume of query-document pairs to train an expansion model. In this
paper, we propose an Unsupervised Document Expansion with Generation (UDEG)
framework with a pre-trained language model, which generates diverse
supplementary sentences for the original document without using labels on
query-document pairs for training. For generating sentences, we further
stochastically perturb their embeddings to generate more diverse sentences for
document expansion. We validate our framework on two standard IR benchmark
datasets. The results show that our framework significantly outperforms
relevant expansion baselines for IR.