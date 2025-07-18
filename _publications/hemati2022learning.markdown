---
layout: publication
title: Learning Binary And Sparse Permutation-invariant Representations For Fast And
  Memory Efficient Whole Slide Image Search
authors: Hemati et al.
conference: Computers in Biology and Medicine
year: 2022
bibkey: hemati2022learning
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.13653'}]
tags: [Image Retrieval, DATASETS, Efficiency And Optimization, Tools & Libraries,
  Evaluation]
---
Learning suitable Whole slide images (WSIs) representations for efficient
retrieval systems is a non-trivial task. The WSI embeddings obtained from
current methods are in Euclidean space not ideal for efficient WSI retrieval.
Furthermore, most of the current methods require high GPU memory due to the
simultaneous processing of multiple sets of patches. To address these
challenges, we propose a novel framework for learning binary and sparse WSI
representations utilizing a deep generative modelling and the Fisher Vector. We
introduce new loss functions for learning sparse and binary
permutation-invariant WSI representations that employ instance-based training
achieving better memory efficiency. The learned WSI representations are
validated on The Cancer Genomic Atlas (TCGA) and Liver-Kidney-Stomach (LKS)
datasets. The proposed method outperforms Yottixel (a recent search engine for
histopathology images) both in terms of retrieval accuracy and speed. Further,
we achieve competitive performance against SOTA on the public benchmark LKS
dataset for WSI classification.