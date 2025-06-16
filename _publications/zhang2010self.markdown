---
layout: publication
title: Self-taught Hashing For Fast Similarity Search
authors: Dell Zhang, Jun Wang, Deng Cai, Jinsong Lu
conference: Arxiv
year: 2010
citations: 252
bibkey: zhang2010self
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1004.5370'}]
tags: [Applications, Unsupervised, ANN Search, Hashing Methods, Supervised, Evaluation
    Metrics]
---
The ability of fast similarity search at large scale is of great importance
to many Information Retrieval (IR) applications. A promising way to accelerate
similarity search is semantic hashing which designs compact binary codes for a
large number of documents so that semantically similar documents are mapped to
similar codes (within a short Hamming distance). Although some recently
proposed techniques are able to generate high-quality codes for documents known
in advance, obtaining the codes for previously unseen documents remains to be a
very challenging problem. In this paper, we emphasise this issue and propose a
novel Self-Taught Hashing (STH) approach to semantic hashing: we first find the
optimal \\(l\\)-bit binary codes for all documents in the given corpus via
unsupervised learning, and then train \\(l\\) classifiers via supervised learning
to predict the \\(l\\)-bit code for any query document unseen before. Our
experiments on three real-world text datasets show that the proposed approach
using binarised Laplacian Eigenmap (LapEig) and linear Support Vector Machine
(SVM) outperforms state-of-the-art techniques significantly.