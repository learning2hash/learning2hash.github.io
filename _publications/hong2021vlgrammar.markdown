---
layout: publication
title: 'Vlgrammar: Grounded Grammar Induction Of Vision And Language'
authors: Yining Hong, Qing Li, Song-Chun Zhu, Siyuan Huang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: hong2021vlgrammar
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.12975'}]
tags: [Evaluation, Supervised, Image Retrieval, ICCV, Self-Supervised, Datasets, Scalability,
  Unsupervised, Tools & Libraries, Text Retrieval]
short_authors: Hong et al.
---
Cognitive grammar suggests that the acquisition of language grammar is
grounded within visual structures. While grammar is an essential representation
of natural language, it also exists ubiquitously in vision to represent the
hierarchical part-whole structure. In this work, we study grounded grammar
induction of vision and language in a joint learning framework. Specifically,
we present VLGrammar, a method that uses compound probabilistic context-free
grammars (compound PCFGs) to induce the language grammar and the image grammar
simultaneously. We propose a novel contrastive learning framework to guide the
joint learning of both modules. To provide a benchmark for the grounded grammar
induction task, we collect a large-scale dataset, \textsc\{PartIt\}, which
contains human-written sentences that describe part-level semantics for 3D
objects. Experiments on the \textsc\{PartIt\} dataset show that VLGrammar
outperforms all baselines in image grammar induction and language grammar
induction. The learned VLGrammar naturally benefits related downstream tasks.
Specifically, it improves the image unsupervised clustering accuracy by 30%,
and performs well in image retrieval and text retrieval. Notably, the induced
grammar shows superior generalizability by easily generalizing to unseen
categories.