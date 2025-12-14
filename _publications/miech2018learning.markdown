---
layout: publication
title: Learning A Text-video Embedding From Incomplete And Heterogeneous Data
authors: Antoine Miech, Ivan Laptev, Josef Sivic
conference: Arxiv
year: 2018
bibkey: miech2018learning
citations: 174
additional_links: [{name: Code, url: 'https://github.com/antoine77340/Mixture-of-Embedding-Experts'},
  {name: Paper, url: 'https://arxiv.org/abs/1804.02516'}]
tags: [Video Retrieval, Datasets, Scalability, Tools & Libraries, Text Retrieval]
short_authors: Antoine Miech, Ivan Laptev, Josef Sivic
---
Joint understanding of video and language is an active research area with
many applications. Prior work in this domain typically relies on learning
text-video embeddings. One difficulty with this approach, however, is the lack
of large-scale annotated video-caption datasets for training. To address this
issue, we aim at learning text-video embeddings from heterogeneous data
sources. To this end, we propose a Mixture-of-Embedding-Experts (MEE) model
with ability to handle missing input modalities during training. As a result,
our framework can learn improved text-video embeddings simultaneously from
image and video datasets. We also show the generalization of MEE to other input
modalities such as face descriptors. We evaluate our method on the task of
video retrieval and report results for the MPII Movie Description and MSR-VTT
datasets. The proposed MEE model demonstrates significant improvements and
outperforms previously reported methods on both text-to-video and video-to-text
retrieval tasks. Code is available at:
https://github.com/antoine77340/Mixture-of-Embedding-Experts