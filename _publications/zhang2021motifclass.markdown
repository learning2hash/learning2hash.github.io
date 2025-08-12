---
layout: publication
title: 'Motifclass: Weakly Supervised Text Classification With Higher-order Metadata
  Information'
authors: Yu Zhang, Shweta Garg, Yu Meng, Xiusi Chen, Jiawei Han
conference: Proceedings of the Fifteenth ACM International Conference on Web Search
  and Data Mining
year: 2022
bibkey: zhang2021motifclass
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04022'}]
tags: ["Supervised"]
short_authors: Zhang et al.
---
We study the problem of weakly supervised text classification, which aims to
classify text documents into a set of pre-defined categories with category
surface names only and without any annotated training document provided. Most
existing classifiers leverage textual information in each document. However, in
many domains, documents are accompanied by various types of metadata (e.g.,
authors, venue, and year of a research paper). These metadata and their
combinations may serve as strong category indicators in addition to textual
contents. In this paper, we explore the potential of using metadata to help
weakly supervised text classification. To be specific, we model the
relationships between documents and metadata via a heterogeneous information
network. To effectively capture higher-order structures in the network, we use
motifs to describe metadata combinations. We propose a novel framework, named
MotifClass, which (1) selects category-indicative motif instances, (2)
retrieves and generates pseudo-labeled training samples based on category names
and indicative motif instances, and (3) trains a text classifier using the
pseudo training data. Extensive experiments on real-world datasets demonstrate
the superior performance of MotifClass to existing weakly supervised text
classification approaches. Further analysis shows the benefit of considering
higher-order metadata information in our framework.