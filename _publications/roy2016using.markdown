---
layout: publication
title: Using Word Embeddings For Automatic Query Expansion
authors: Dwaipayan Roy, Debjyoti Paul, Mandar Mitra, Utpal Garain
conference: Arxiv
year: 2016
bibkey: roy2016using
citations: 86
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07608'}]
tags: ["Evaluation", "Tools & Libraries", "Unsupervised"]
short_authors: Roy et al.
---
In this paper a framework for Automatic Query Expansion (AQE) is proposed
using distributed neural language model word2vec. Using semantic and contextual
relation in a distributed and unsupervised framework, word2vec learns a low
dimensional embedding for each vocabulary entry. Using such a framework, we
devise a query expansion technique, where related terms to a query are obtained
by K-nearest neighbor approach. We explore the performance of the AQE methods,
with and without feedback query expansion, and a variant of simple K-nearest
neighbor in the proposed framework. Experiments on standard TREC ad-hoc data
(Disk 4, 5 with query sets 301-450, 601-700) and web data (WT10G data with
query set 451-550) shows significant improvement over standard term-overlapping
based retrieval methods. However the proposed method fails to achieve
comparable performance with statistical co-occurrence based feedback method
such as RM3. We have also found that the word2vec based query expansion methods
perform similarly with and without any feedback information.