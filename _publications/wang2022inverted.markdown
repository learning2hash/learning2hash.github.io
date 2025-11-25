---
layout: publication
title: Inverted Semantic-index For Image Retrieval
authors: Ying Wang
conference: Arxiv
year: 2022
bibkey: wang2022inverted
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.12623'}]
tags: ["Evaluation", "Image Retrieval", "Quantization", "Scalability", "Supervised"]
short_authors: Ying Wang
---
This paper addresses the construction of inverted index for large-scale image
retrieval. The inverted index proposed by J. Sivic brings a significant
acceleration by reducing distance computations with only a small fraction of
the database. The state-of-the-art inverted indices aim to build finer
partitions that produce a concise and accurate candidate list. However,
partitioning in these frameworks is generally achieved by unsupervised
clustering methods which ignore the semantic information of images. In this
paper, we replace the clustering method with image classification, during the
construction of codebook. We then propose a merging and splitting method to
solve the problem that the number of partitions is unchangeable in the inverted
semantic-index. Next, we combine our semantic-index with the product
quantization (PQ) so as to alleviate the accuracy loss caused by PQ
compression. Finally, we evaluate our model on large-scale image retrieval
benchmarks. Experiment results demonstrate that our model can significantly
improve the retrieval accuracy by generating high-quality candidate lists.