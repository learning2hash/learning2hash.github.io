---
layout: publication
title: Supervised Deep Hashing For High45;dimensional And Heterogeneous Case45;based Reasoning
authors: Zhang Qi, Hu Liang, Shi Chongyang, Liu Ke, Cao Longbing
conference: "Arxiv"
year: 2022
bibkey: zhang2022supervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2206.14523"}
tags: ['ARXIV', 'Cross Modal', 'Quantisation', 'Supervised']
---
Case45;based Reasoning (CBR) on high45;dimensional and heterogeneous data is a trending yet challenging and computationally expensive task in the real world. A promising approach is to obtain low45;dimensional hash codes representing cases and perform a similarity retrieval of cases in Hamming space. However previous methods based on data45;independent hashing rely on random projections or manual construction inapplicable to address specific data issues (e.g. high45;dimensionality and heterogeneity) due to their insensitivity to data characteristics. To address these issues this work introduces a novel deep hashing network to learn similarity45;preserving compact hash codes for efficient case retrieval and proposes a deep45;hashing45;enabled CBR model HeCBR. Specifically we introduce position embedding to represent heterogeneous features and utilize a multilinear interaction layer to obtain case embeddings which effectively filtrates zero45;valued features to tackle high45;dimensionality and sparsity and captures inter45;feature couplings. Then we feed the case embeddings into fully45;connected layers and subsequently a hash layer generates hash codes with a quantization regularizer to control the quantization loss during relaxation. To cater to incremental learning of CBR we further propose an adaptive learning strategy to update the hash function. Extensive experiments on public datasets show that HeCBR greatly reduces storage and significantly accelerates case retrieval. HeCBR achieves desirable performance compared with the state45;of45;the45;art CBR methods and performs significantly better than hashing45;based CBR methods in classification.
