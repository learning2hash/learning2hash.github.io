---
layout: publication
title: Norm45;ranging LSH For Maximum Inner Product Search
authors: Xiao Yan, Jinfeng Li, Xinyan Dai, Hongzhi Chen, James Cheng
conference: "Neural Information Processing Systems"
year: 2018
bibkey: yan2018lsh
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2018/hash/b60c5ab647a27045b462934977ccad9a-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
Neyshabur and Srebro proposed SIMPLE45;LSH which is the state45;of45;the45;art hashing based algorithm for maximum inner product search (MIPS). We found that the performance of SIMPLE45;LSH in both theory and practice suffers from long tails in the 245;norm distribution of real datasets. We propose NORM45;RANGING LSH which addresses the excessive normalization problem caused by long tails by partitioning a dataset into sub45;datasets and building a hash index for each sub45;dataset independently. We prove that NORM45;RANGING LSH achieves lower query time complexity than SIMPLE45;LSH under mild conditions. We also show that the idea of dataset partitioning can improve another hashing based MIPS algorithm. Experiments show that NORM45;RANGING LSH probes much less items than SIMPLE45;LSH at the same recall thus significantly benefiting MIPS based applications.
