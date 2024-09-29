---
layout: publication
title: Beyond Neighbourhood45;preserving Transformations For Quantization45;based Unsupervised Hashing
authors: Hemati Sobhan, Tizhoosh H. R.
conference: "Arxiv"
year: 2021
bibkey: hemati2021beyond
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2110.00216"}
tags: ['ARXIV', 'Quantisation', 'Unsupervised']
---
An effective unsupervised hashing algorithm leads to compact binary codes preserving the neighborhood structure of data as much as possible. One of the most established schemes for unsupervised hashing is to reduce the dimensionality of data and then find a rigid (neighbourhood45;preserving) transformation that reduces the quantization error. Although employing rigid transformations is effective we may not reduce quantization loss to the ultimate limits. As well reducing dimensionality and quantization loss in two separate steps seems to be sub45;optimal. Motivated by these shortcomings we propose to employ both rigid and non45;rigid transformations to reduce quantization error and dimensionality simultaneously. We relax the orthogonality constraint on the projection in a PCA45;formulation and regularize this by a quantization term. We show that both the non45;rigid projection matrix and rotation matrix contribute towards minimizing quantization loss but in different ways. A scalable nested coordinate descent approach is proposed to optimize this mixed45;integer optimization problem. We evaluate the proposed method on five public benchmark datasets providing almost half a million images. Comparative results indicate that the proposed method mostly outperforms state45;of45;art linear methods and competes with end45;to45;end deep solutions.
