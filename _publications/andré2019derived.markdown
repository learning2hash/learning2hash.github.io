---
layout: publication
title: Derived Codebooks For High-accuracy Nearest Neighbor Search
authors: "Fabien Andr\xE9, Anne-marie Kermarrec, Nicolas Le Scouarnec"
conference: Arxiv
year: 2019
citations: 1
bibkey: "andr\xE92019derived"
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.06900'}]
tags: [Indexing, Evaluation Metrics, ANN Search, Quantization]
---
High-dimensional Nearest Neighbor (NN) search is central in multimedia search
systems. Product Quantization (PQ) is a widespread NN search technique which
has a high performance and good scalability. PQ compresses high-dimensional
vectors into compact codes thanks to a combination of quantizers. Large
databases can, therefore, be stored entirely in RAM, enabling fast responses to
NN queries. In almost all cases, PQ uses 8-bit quantizers as they offer low
response times. In this paper, we advocate the use of 16-bit quantizers.
Compared to 8-bit quantizers, 16-bit quantizers boost accuracy but they
increase response time by a factor of 3 to 10. We propose a novel approach that
allows 16-bit quantizers to offer the same response time as 8-bit quantizers,
while still providing a boost of accuracy. Our approach builds on two key
ideas: (i) the construction of derived codebooks that allow a fast and
approximate distance evaluation, and (ii) a two-pass NN search procedure which
builds a candidate set using the derived codebooks, and then refines it using
16-bit quantizers. On 1 billion SIFT vectors, with an inverted index, our
approach offers a Recall@100 of 0.85 in 5.2 ms. By contrast, 16-bit quantizers
alone offer a Recall@100 of 0.85 in 39 ms, and 8-bit quantizers a Recall@100 of
0.82 in 3.8 ms.