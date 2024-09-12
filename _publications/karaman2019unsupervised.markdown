---
layout: publication
title: Unsupervised Rank-Preserving Hashing for Large-Scale Image Retrieval
authors: Karaman Svebor, Lin Xudong, Hu Xuefeng, Chang Shih-Fu
conference: "Arxiv"
year: 2019
bibkey: karaman2019unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1903.01545"}
tags: ['ARXIV', 'Graph', 'Image Retrieval', 'TIP', 'Unsupervised']
---
We propose an unsupervised hashing method which aims to produce binary codes that preserve the ranking induced by a real-valued representation. Such compact hash codes enable the complete elimination of real-valued feature storage and allow for significant reduction of the computation complexity and storage cost of large-scale image retrieval applications. Specifically we learn a neural network-based model which transforms the input representation into a binary representation. We formalize the training objective of the network in an intuitive and effective way considering each training sample as a query and aiming to obtain the same retrieval results using the produced hash codes as those obtained with the original features. This training formulation directly optimizes the hashing model for the target usage of the hash codes it produces. We further explore the addition of a decoder trained to obtain an approximated reconstruction of the original features. At test time we retrieved the most promising database samples with an efficient graph-based search procedure using only our hash codes and perform re-ranking using the reconstructed features thus without needing to access the original features at all. Experiments conducted on multiple publicly available large-scale datasets show that our method consistently outperforms all compared state-of-the-art unsupervised hashing methods and that the reconstruction procedure can effectively boost the search accuracy with a minimal constant additional cost.
