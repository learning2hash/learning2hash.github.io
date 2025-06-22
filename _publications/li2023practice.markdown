---
layout: publication
title: 'Practice With Graph-based ANN Algorithms On Sparse Data: Chi-square Two-tower
  Model, HNSW, Sign Cauchy Projections'
authors: Ping Li et al.
conference: Arxiv
year: 2023
citations: 0
bibkey: li2023practice
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.07607'}]
tags: [Applications, Tools and Libraries, ANN Search, Efficient Learning, Evaluation
    Metrics]
---
Sparse data are common. The traditional ``handcrafted'' features are often
sparse. Embedding vectors from trained models can also be very sparse, for
example, embeddings trained via the ``ReLu'' activation function. In this
paper, we report our exploration of efficient search in sparse data with
graph-based ANN algorithms (e.g., HNSW, or SONG which is the GPU version of
HNSW), which are popular in industrial practice, e.g., search and ads
(advertising).
  We experiment with the proprietary ads targeting application, as well as
benchmark public datasets. For ads targeting, we train embeddings with the
standard ``cosine two-tower'' model and we also develop the ``chi-square
two-tower'' model. Both models produce (highly) sparse embeddings when they are
integrated with the ``ReLu'' activation function. In EBR (embedding-based
retrieval) applications, after we the embeddings are trained, the next crucial
task is the approximate near neighbor (ANN) search for serving. While there are
many ANN algorithms we can choose from, in this study, we focus on the
graph-based ANN algorithm (e.g., HNSW-type).
  Sparse embeddings should help improve the efficiency of EBR. One benefit is
the reduced memory cost for the embeddings. The other obvious benefit is the
reduced computational time for evaluating similarities, because, for
graph-based ANN algorithms such as HNSW, computing similarities is often the
dominating cost. In addition to the effort on leveraging data sparsity for
storage and computation, we also integrate ``sign cauchy random projections''
(SignCRP) to hash vectors to bits, to further reduce the memory cost and speed
up the ANN search. In NIPS'13, SignCRP was proposed to hash the chi-square
similarity, which is a well-adopted nonlinear kernel in NLP and computer
vision. Therefore, the chi-square two-tower model, SignCRP, and HNSW are now
tightly integrated.