---
layout: publication
title: Norm-ranging LSH For Maximum Inner Product Search
authors: Xiao Yan, Jinfeng Li, Xinyan Dai, Hongzhi Chen, James Cheng
conference: "Neural Information Processing Systems"
year: 2018
bibkey: yan2018norm
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2018/hash/b60c5ab647a27045b462934977ccad9a-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS', 'Theory']
---
Neyshabur and Srebro proposed SIMPLE-LSH, which is the state-of-the-art hashing based algorithm for maximum inner product search (MIPS). We found that the performance of SIMPLE-LSH, in both theory and practice, suffers from long tails in the 2-norm distribution of real datasets. We propose NORM-RANGING LSH, which addresses the excessive normalization problem caused by long tails by partitioning a dataset into sub-datasets and building a hash index for each sub-dataset independently. We prove that NORM-RANGING LSH achieves lower query time complexity than SIMPLE-LSH under mild conditions. We also show that the idea of dataset partitioning can improve another hashing based MIPS algorithm. Experiments show that NORM-RANGING LSH probes much less items than SIMPLE-LSH at the same recall, thus significantly benefiting MIPS based applications.
