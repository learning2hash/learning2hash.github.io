---
layout: publication
title: Norm-Ranging LSH for Maximum Inner Product Search
authors: X I A O Y A N, J I N F E N G L I, X I N Y A N D A I, H O N G Z H I C H E N, J A M E S C H E N G
conference: "Neural Information Processing Systems"
year: 2018
bibkey: yan2018normranging
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2018/hash/b60c5ab647a27045b462934977ccad9a-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
Neyshabur and Srebro proposed SIMPLE-LSH which is the state-of-the-art hashing based algorithm for maximum inner product search (MIPS). We found that the performance of SIMPLE-LSH in both theory and practice suffers from long tails in the 2-norm distribution of real datasets. We propose NORM-RANGING LSH which addresses the excessive normalization problem caused by long tails by partitioning a dataset into sub-datasets and building a hash index for each sub-dataset independently. We prove that NORM-RANGING LSH achieves lower query time complexity than SIMPLE-LSH under mild conditions. We also show that the idea of dataset partitioning can improve another hashing based MIPS algorithm. Experiments show that NORM-RANGING LSH probes much less items than SIMPLE-LSH at the same recall thus significantly benefiting MIPS based applications.
