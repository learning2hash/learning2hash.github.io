---
layout: publication
title: SLOSH Set LOcality Sensitive Hashing via Sliced-Wasserstein Embeddings
authors: Lu Yuzhe, Liu Xinran, Soltoggio Andrea, Kolouri Soheil
conference: "Arxiv"
year: 2021
bibkey: lu2021slosh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.05872"}
tags: ['ARXIV', 'Independent']
---
Learning from set-structured data is an essential problem with many applications in machine learning and computer vision. This paper focuses on non-parametric and data-independent learning from set-structured data using approximate nearest neighbor (ANN) solutions particularly locality-sensitive hashing. We consider the problem of set retrieval from an input set query. Such retrieval problem requires 1) an efficient mechanism to calculate the distances/dissimilarities between sets and 2) an appropriate data structure for fast nearest neighbor search. To that end we propose Sliced-Wasserstein set embedding as a computationally efficient set-2-vector mechanism that enables downstream ANN with theoretical guarantees. The set elements are treated as samples from an unknown underlying distribution and the Sliced-Wasserstein distance is used to compare sets. We demonstrate the effectiveness of our algorithm denoted as Set-LOcality Sensitive Hashing (SLOSH) on various set retrieval datasets and compare our proposed embedding with standard set embedding approaches including Generalized Mean (GeM) embedding/pooling Featurewise Sort Pooling (FSPool) and Covariance Pooling and show consistent improvement in retrieval results. The code for replicating our results is available here httpsgithub.com/mint-vu/SLOSH.
