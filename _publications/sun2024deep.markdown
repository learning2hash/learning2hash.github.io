---
layout: publication
title: Deep Normalized Cross-modal Hashing With Bi-direction Relation Reasoning
authors: Sun Changchang, Latapie, Liu, Yan
conference: "Arxiv"
year: 2024
bibkey: sun2024deep
additional_links:
  - {name: "Paper", url: "https://openaccess.thecvf.com/content/CVPR2022W/ODRUM/papers/Sun_Deep_Normalized_Cross-Modal_Hashing_With_Bi-Direction_Relation_Reasoning_CVPRW_2022_paper.pdf"}
tags: ['ARXIV', 'Cross Modal', 'Independent']
---
Due to the continuous growth of large-scale multi-modal data and increasing requirements for retrieval speed, deep cross-modal hashing has gained increasing attention recently. Most of existing studies take a similarity matrix as supervision to optimize their models, and the inner product between continuous surrogates of hash codes is utilized to depict the similarity in the Hamming space. However, all of them merely consider the relevant information to build the similarity matrix, ignoring the contribution of the irrelevant one, i.e., the categories that samples do not belong to. Therefore, they cannot effectively alleviate the effect of dissimilar samples. Moreover, due to the modality distribution difference, directly utilizing continuous surrogates of hash codes to calculate similarity may induce suboptimal retrieval performance. To tackle these issues, in this paper, we propose a novel deep normalized cross-modal hashing scheme with bi-direction relation reasoning, named Bi_NCMH. Specifically, we build the multi-level semantic similarity matrix by considering bi-direction relation, i.e., consistent and inconsistent relation. It hence can holistically characterize relations among instances. Besides, we execute feature normalization on continuous surrogates of hash codes to eliminate the deviation caused by modality gap, which further reduces the negative impact of binarization on retrieval performance. Extensive experiments on two cross-modal benchmark datasets demonstrate the superiority of our model over several state-of-the-art baselines.
