---
layout: publication
title: Indexing Of CNN Features For Large Scale Image Search
authors: Liu Ruoyu, Zhao Yao, Wei Shikui, Yang Yi
conference: "Arxiv"
year: 2015
bibkey: liu2015indexing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1508.00217"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Quantisation', 'Unsupervised']
---
<p>The convolutional neural network (CNN) features can give a good
description of image content, which usually represent images with unique
global vectors. Although they are compact compared to local descriptors,
they still cannot efficiently deal with large-scale image retrieval due
to the cost of the linear incremental computation and storage. To
address this issue, we build a simple but effective indexing framework
based on inverted table, which significantly decreases both the search
time and memory usage. In addition, several strategies are fully
investigated under an indexing framework to adapt it to CNN features and
compensate for quantization errors. First, we use multiple assignment
for the query and database images to increase the probability of
relevant images’ co-existing in the same Voronoi cells obtained via the
clustering algorithm. Then, we introduce embedding codes to further
improve precision by removing false matches during a search. We
demonstrate that by using hashing schemes to calculate the embedding
codes and by changing the ranking rule, indexing framework speeds can be
greatly improved. Extensive experiments conducted on several
unsupervised and supervised benchmarks support these results and the
superiority of the proposed indexing framework. We also provide a fair
comparison between the popular CNN features.</p>
