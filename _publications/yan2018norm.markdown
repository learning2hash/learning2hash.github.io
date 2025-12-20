---
layout: publication
title: Norm-ranging LSH For Maximum Inner Product Search
authors: Xiao Yan, Jinfeng Li, Xinyan Dai, Hongzhi Chen, James Cheng
conference: Arxiv
year: 2018
bibkey: yan2018norm
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.08782'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Yan et al.
---
Neyshabur and Srebro proposed Simple-LSH, which is the state-of-the-art
hashing method for maximum inner product search (MIPS) with performance
guarantee. We found that the performance of Simple-LSH, in both theory and
practice, suffers from long tails in the 2-norm distribution of real datasets.
We propose Norm-ranging LSH, which addresses the excessive normalization
problem caused by long tails in Simple-LSH by partitioning a dataset into
multiple sub-datasets and building a hash index for each sub-dataset
independently. We prove that Norm-ranging LSH has lower query time complexity
than Simple-LSH. We also show that the idea of partitioning the dataset can
improve other hashing based methods for MIPS. To support efficient query
processing on the hash indexes of the sub-datasets, a novel similarity metric
is formulated. Experiments show that Norm-ranging LSH achieves an order of
magnitude speedup over Simple-LSH for the same recall, thus significantly
benefiting applications that involve MIPS.