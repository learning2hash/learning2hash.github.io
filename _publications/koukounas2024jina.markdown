---
layout: publication
title: 'Jina CLIP: Your CLIP Model Is Also Your Text Retriever'
authors: "Andreas Koukounas, Georgios Mastrapas, Michael G\xFCnther, Bo Wang, Scott\
  \ Martens, Isabelle Mohr, Saba Sturua, Mohammad Kalim Akram, Joan Fontanals Mart\xED\
  nez, Saahil Ognawala, Susana Guzman, Maximilian Werk, Nan Wang, Han Xiao"
conference: Arxiv
year: 2024
bibkey: koukounas2024jina
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.20204'}]
tags: [Text Retrieval, Evaluation, Efficiency]
short_authors: Koukounas et al.
---
Contrastive Language-Image Pretraining (CLIP) is widely used to train models
to align images and texts in a common embedding space by mapping them to
fixed-sized vectors. These models are key to multimodal information retrieval
and related tasks. However, CLIP models generally underperform in text-only
tasks compared to specialized text models. This creates inefficiencies for
information retrieval systems that keep separate embeddings and models for
text-only and multimodal tasks. We propose a novel, multi-task contrastive
training method to address this issue, which we use to train the jina-clip-v1
model to achieve the state-of-the-art performance on both text-image and
text-text retrieval tasks.