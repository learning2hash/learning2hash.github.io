---
layout: publication
title: Fuzzy Hashing as Perturbation-Consistent Adversarial Kernel Embedding
authors: Azarafrooz Ari, Brock John
conference: "Arxiv"
year: 2018
bibkey: azarafrooz2018fuzzy
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1812.07071"}
tags: ['ARXIV']
---
Measuring the similarity of two files is an important task in malware analysis with fuzzy hash functions being a popular approach. Traditional fuzzy hash functions are data agnostic they do not learn from a particular dataset how to determine similarity; their behavior is fixed across all datasets. In this paper we demonstrate that fuzzy hash functions can be learned in a novel minimax training framework and that these learned fuzzy hash functions outperform traditional fuzzy hash functions at the file similarity task for Portable Executable files. In our approach hash digests can be extracted from the kernel embeddings of two kernel networks trained in a minimax framework where the roles of players during training (i.e adversary versus generator) alternate along with the input data. We refer to this new minimax architecture as perturbation-consistent. The similarity score for a pair of files is the utility of the minimax game in equilibrium. Our experiments show that learned fuzzy hash functions generalize well capable of determining that two files are similar even when one of those files was generated using insertion and deletion operations.
