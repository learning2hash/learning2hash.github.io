---
layout: publication
title: Learning Binary Hash Codes For Large-scale Image Search
authors: Kristen Grauman, Fergus
conference: Studies in Computational Intelligence
year: 2025
bibkey: grauman2025learning
citations: 100
additional_links: [{name: Paper, url: 'https://link.springer.com/chapter/10.1007/978-3-642-28661-2_3'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Large Scale Search", "Supervised", "Unsupervised"]
short_authors: Kristen Grauman, Fergus
---
Algorithms to rapidly search massive image or video collections are critical for many vision applications, including visual search, content-based retrieval, and non-parametric models for object recognition. Recent work shows that learned binary projections are a powerful way to index large collections according to their content. The basic idea is to formulate the projections so as to approximately preserve a given similarity function of interest. Having done so, one can then search the data efficiently using hash tables, or by exploring the Hamming ball volume around a novel query. Both enable sub-linear time retrieval with respect to the database size. Further, depending on the design of the projections, in some cases it is possible to bound the number of database examples that must be searched in order to achieve a given level of accuracy.

This chapter overviews data structures for fast search with binary codes, and then describes several supervised and unsupervised strategies for generating the codes. In particular, we review supervised methods that integrate metric learning, boosting, and neural networks into the hash key construction, and unsupervised methods based on spectral analysis or kernelized random projections that compute affinity-preserving binary codes.Whether learning from explicit semantic supervision or exploiting the structure among unlabeled data, these methods make scalable retrieval possible for a variety of robust visual similarity measures.We focus on defining the algorithms, and illustrate the main points with results using millions of images.