---
layout: publication
title: A Neighbourhood-aware Differential Privacy Mechanism For Static Word Embeddings
authors: Danushka Bollegala, Shuichi Otake, Tomoya MacHide, Ken-Ichi Kawarabayashi
conference: 'Findings of the Association for Computational Linguistics: IJCNLP-AACL
  2023 (Findings)'
year: 2023
bibkey: bollegala2023a
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.10551'}]
tags: [Privacy & Security, ACL]
short_authors: Bollegala et al.
---
We propose a Neighbourhood-Aware Differential Privacy (NADP) mechanism
considering the neighbourhood of a word in a pretrained static word embedding
space to determine the minimal amount of noise required to guarantee a
specified privacy level. We first construct a nearest neighbour graph over the
words using their embeddings, and factorise it into a set of connected
components (i.e. neighbourhoods). We then separately apply different levels of
Gaussian noise to the words in each neighbourhood, determined by the set of
words in that neighbourhood. Experiments show that our proposed NADP mechanism
consistently outperforms multiple previously proposed DP mechanisms such as
Laplacian, Gaussian, and Mahalanobis in multiple downstream tasks, while
guaranteeing higher levels of privacy.