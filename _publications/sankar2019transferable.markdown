---
layout: publication
title: Transferable Neural Projection Representations
authors: Sankar Chinnadhurai, Ravi Sujith, Kozareva Zornitsa
conference: "Proc. of NAACL"
year: 2019
bibkey: sankar2019transferable
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1906.01605"}
tags: ['LSH', 'Unsupervised']
---
Neural word representations are at the core of many state-of-the-art natural language processing models. A widely used approach is to pre-train store and look up word or character embedding matrices. While useful such representations occupy huge memory making it hard to deploy on-device and often do not generalize to unknown words due to vocabulary pruning. In this paper we propose a skip-gram based architecture coupled with Locality-Sensitive Hashing (LSH) projections to learn efficient dynamically computable representations. Our model does not need to store lookup tables as representations are computed on-the-fly and require low memory footprint. The representations can be trained in an unsupervised fashion and can be easily transferred to other NLP tasks. For qualitative evaluation we analyze the nearest neighbors of the word representations and discover semantically similar words even with misspellings. For quantitative evaluation we plug our transferable projections into a simple LSTM and run it on multiple NLP tasks and show how our transferable projections achieve better performance compared to prior work.
