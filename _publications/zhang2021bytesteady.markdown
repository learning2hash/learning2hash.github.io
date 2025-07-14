---
layout: publication
title: Bytesteady Fast Classification Using Byte-level N-gram Embeddings
authors: Zhang Xiang, Drouin Alexandre, Li Raymond
conference: Arxiv
year: 2021
citations: 1
bibkey: zhang2021bytesteady
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.13302'}]
tags: [ARXIV, Supervised]
---
This article introduces byteSteady -- a fast model for classification using
byte-level n-gram embeddings. byteSteady assumes that each input comes as a
sequence of bytes. A representation vector is produced using the averaged
embedding vectors of byte-level n-grams, with a pre-defined set of n. The
hashing trick is used to reduce the number of embedding vectors. This input
representation vector is then fed into a linear classifier. A straightforward
application of byteSteady is text classification. We also apply byteSteady to
one type of non-language data -- DNA sequences for gene classification. For
both problems we achieved competitive classification results against strong
baselines, suggesting that byteSteady can be applied to both language and
non-language data. Furthermore, we find that simple compression using Huffman
coding does not significantly impact the results, which offers an
accuracy-speed trade-off previously unexplored in machine learning.