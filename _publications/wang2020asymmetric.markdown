---
layout: publication
title: Asymmetric Correlation Quantization Hashing For Cross-modal Retrieval
authors: Wang Lu, Yang Jie
conference: "Arxiv"
year: 2020
bibkey: wang2020asymmetric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2001.04625"}
tags: ['ARXIV', 'Cross Modal', 'Quantisation', 'Supervised']
---
<p>Due to the superiority in similarity computation and database storage
for large-scale multiple modalities data, cross-modal hashing methods
have attracted extensive attention in similarity retrieval across the
heterogeneous modalities. However, there are still some limitations to
be further taken into account: (1) most current CMH methods transform
real-valued data points into discrete compact binary codes under the
binary constraints, limiting the capability of representation for
original data on account of abundant loss of information and producing
suboptimal hash codes; (2) the discrete binary constraint learning model
is hard to solve, where the retrieval performance may greatly reduce by
relaxing the binary constraints for large quantization error; (3)
handling the learning problem of CMH in a symmetric framework, leading
to difficult and complex optimization objective. To address above
challenges, in this paper, a novel Asymmetric Correlation Quantization
Hashing (ACQH) method is proposed. Specifically, ACQH learns the
projection matrixs of heterogeneous modalities data points for
transforming query into a low-dimensional real-valued vector in latent
semantic space and constructs the stacked compositional quantization
embedding in a coarse-to-fine manner for indicating database points by a
series of learnt real-valued codeword in the codebook with the help of
pointwise label information regression simultaneously. Besides, the
unified hash codes across modalities can be directly obtained by the
discrete iterative optimization framework devised in the paper.
Comprehensive experiments on diverse three benchmark datasets have shown
the effectiveness and rationality of ACQH.</p>
