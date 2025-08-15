---
layout: publication
title: 'Pqk-means: Billion-scale Clustering For Product-quantized Codes'
authors: Yusuke Matsui, Keisuke Ogaki, Toshihiko Yamasaki, Kiyoharu Aizawa
conference: Arxiv
year: 2017
bibkey: matsui2017pqk
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.03708'}]
tags: ["Quantization", "Scalability"]
short_authors: Matsui et al.
---
Data clustering is a fundamental operation in data analysis. For handling
large-scale data, the standard k-means clustering method is not only slow, but
also memory-inefficient. We propose an efficient clustering method for
billion-scale feature vectors, called PQk-means. By first compressing input
vectors into short product-quantized (PQ) codes, PQk-means achieves fast and
memory-efficient clustering, even for high-dimensional vectors. Similar to
k-means, PQk-means repeats the assignment and update steps, both of which can
be performed in the PQ-code domain. Experimental results show that even
short-length (32 bit) PQ-codes can produce competitive results compared with
k-means. This result is of practical importance for clustering in
memory-restricted environments. Using the proposed PQk-means scheme, the
clustering of one billion 128D SIFT features with K = 10^5 is achieved within
14 hours, using just 32 GB of memory consumption on a single computer.