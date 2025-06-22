---
layout: publication
title: Variant Tolerant Read Mapping Using Min-hashing
authors: Jens Quedenfeld, Sven Rahmann
conference: Arxiv
year: 2017
citations: 4
bibkey: quedenfeld2017variant
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.01703'}, {name: Code,
    url: 'https://bitbucket.org/Quedenfeld/vatram-src/'}]
tags: [Hashing Methods, Has Code, Evaluation Metrics, ANN Search]
---
DNA read mapping is a ubiquitous task in bioinformatics, and many tools have
been developed to solve the read mapping problem. However, there are two trends
that are changing the landscape of readmapping: First, new sequencing
technologies provide very long reads with high error rates (up to 15%). Second,
many genetic variants in the population are known, so the reference genome is
not considered as a single string over ACGT, but as a complex object containing
these variants. Most existing read mappers do not handle these new
circumstances appropriately.
  We introduce a new read mapper prototype called VATRAM that considers
variants. It is based on Min-Hashing of q-gram sets of reference genome
windows. Min-Hashing is one form of locality sensitive hashing. The variants
are directly inserted into VATRAMs index which leads to a fast mapping process.
Our results show that VATRAM achieves better precision and recall than
state-of-the-art read mappers like BWA under certain cirumstances. VATRAM is
open source and can be accessed at
https://bitbucket.org/Quedenfeld/vatram-src/.