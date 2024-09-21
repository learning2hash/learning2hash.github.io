---
layout: publication
title: Cross-Domain Matching for Bag-of-Words Data via Kernel Embeddings of Latent Distributions
authors: Y U Y A Y O S H I K A W A, T O M O H A R U I W A T A, H I R O S H I S A W A D A, T A K E S H I Y A M A D A
conference: "Neural Information Processing Systems"
year: 2015
bibkey: yoshikawa2015cross
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2015/hash/fc49306d97602c8ed1be1dfbf0835ead-Abstract.html"}
tags: ['Cross Modal', 'NEURIPS']
---
We propose a kernel-based method for finding matching between instances across different domains such as multilingual documents and images with annotations. Each instance is assumed to be represented as a multiset of features e.g. a bag-of-words representation for documents. The major difficulty in finding cross-domain relationships is that the similarity between instances in different domains cannot be directly measured. To overcome this difficulty the proposed method embeds all the features of different domains in a shared latent space and regards each instance as a distribution of its own features in the shared latent space. To represent the distributions efficiently and nonparametrically we employ the framework of the kernel embeddings of distributions. The embedding is estimated so as to minimize the difference between distributions of paired instances while keeping unpaired instances apart. In our experiments we show that the proposed method can achieve high performance on finding correspondence between multi-lingual Wikipedia articles between documents and tags and between images and tags.
