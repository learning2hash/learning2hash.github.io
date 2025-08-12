---
layout: publication
title: Encoding High-cardinality String Categorical Variables
authors: "Patricio Cerda, Ga\xEBl Varoquaux"
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: cerda2019encoding
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.01860'}]
tags: ["Scalability"]
short_authors: "Patricio Cerda, Ga\xEBl Varoquaux"
---
Statistical models usually require vector representations of categorical
variables, using for instance one-hot encoding. This strategy breaks down when
the number of categories grows, as it creates high-dimensional feature vectors.
Additionally, for string entries, one-hot encoding does not capture information
in their representation.Here, we seek low-dimensional encoding of
high-cardinality string categorical variables. Ideally, these should be:
scalable to many categories; interpretable to end users; and facilitate
statistical analysis. We introduce two encoding approaches for string
categories: a Gamma-Poisson matrix factorization on substring counts, and the
min-hash encoder, for fast approximation of string similarities. We show that
min-hash turns set inclusions into inequality relations that are easier to
learn. Both approaches are scalable and streamable. Experiments on real and
simulated data show that these methods improve supervised learning with
high-cardinality categorical variables. We recommend the following: if
scalability is central, the min-hash encoder is the best option as it does not
require any data fit; if interpretability is important, the Gamma-Poisson
factorization is the best alternative, as it can be interpreted as one-hot
encoding on inferred categories with informative feature names. Both models
enable autoML on the original string entries as they remove the need for
feature engineering or data cleaning.