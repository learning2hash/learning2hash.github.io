---
layout: publication
title: Disease Classification In Metagenomics With 2D Embeddings And Deep Learning
authors: Thanh Hai Nguyen, Edi Prifti, Yann Chevaleyre, Nataliya Sokolovska, Jean-Daniel
  Zucker
conference: Arxiv
year: 2018
bibkey: nguyen2018disease
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.09046'}]
tags: []
short_authors: Nguyen et al.
---
Deep learning (DL) techniques have shown unprecedented success when applied
to images, waveforms, and text. Generally, when the sample size (\(N\)) is much
bigger than the number of features (\(d\)), DL often outperforms other machine
learning (ML) techniques, often through the use of Convolutional Neural
Networks (CNNs). However, in many bioinformatics fields (including
metagenomics), we encounter the opposite situation where \(d\) is significantly
greater than \(N\). In these situations, applying DL techniques would lead to
severe overfitting.
  Here we aim to improve classification of various diseases with metagenomic
data through the use of CNNs. For this we proposed to represent metagenomic
data as images. The proposed Met2Img approach relies on taxonomic and t-SNE
embeddings to transform abundance data into "synthetic images".
  We applied our approach to twelve benchmark data sets including more than
1400 metagenomic samples. Our results show significant improvements over the
state-of-the-art algorithms (Random Forest (RF), Support Vector Machine (SVM)).
We observe that the integration of phylogenetic information alongside abundance
data improves classification. The proposed approach is not only important in
classification setting but also allows to visualize complex metagenomic data.
The Met2Img is implemented in Python.