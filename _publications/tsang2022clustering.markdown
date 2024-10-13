---
layout: publication
title: Clustering The Sketch A Novel Approach To Embedding Table Compression
authors: Tsang Henry Ling-hei, Ahle Thomas Dybdahl
conference: "Arxiv"
year: 2022
bibkey: tsang2022clustering
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2210.05974"}
tags: ['ARXIV', 'Quantisation', 'Unsupervised']
---
<p>Embedding tables are used by machine learning systems to work with
categorical features. In modern Recommendation Systems, these tables can
be very large, necessitating the development of new methods for fitting
them in memory, even during training. We suggest Clustered Compositional
Embeddings (CCE) which combines clustering-based compression like
quantization to codebooks with dynamic methods like The Hashing Trick
and Compositional Embeddings (Shi et al., 2020). Experimentally CCE
achieves the best of both worlds: The high compression rate of
codebook-based quantization, but <em>dynamically</em> like hashing-based
methods, so it can be used during training. Theoretically, we prove that
CCE is guaranteed to converge to the optimal codebook and give a tight
bound for the number of iterations required.</p>
