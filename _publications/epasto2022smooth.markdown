---
layout: publication
title: Smooth Anonymity For Sparse Graphs
authors: Alessandro Epasto, Hossein Esfandiari, Vahab Mirrokni, Andres Munoz Medina
conference: Companion Proceedings of the ACM Web Conference 2024
year: 2024
bibkey: epasto2022smooth
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.06358'}]
tags: []
short_authors: Epasto et al.
---
When working with user data providing well-defined privacy guarantees is
paramount. In this work, we aim to manipulate and share an entire sparse
dataset with a third party privately. In fact, differential privacy has emerged
as the gold standard of privacy, however, when it comes to sharing sparse
datasets, e.g. sparse networks, as one of our main results, we prove that
*any* differentially private mechanism that maintains a reasonable
similarity with the initial dataset is doomed to have a very weak privacy
guarantee. In such situations, we need to look into other privacy notions such
as \\(k\\)-anonymity. In this work, we consider a variation of \\(k\\)-anonymity, which
we call smooth-\\(k\\)-anonymity, and design simple large-scale algorithms that
efficiently provide smooth-\\(k\\)-anonymity. We further perform an empirical
evaluation to back our theoretical guarantees and show that our algorithm
improves the performance in downstream machine learning tasks on anonymized
data.