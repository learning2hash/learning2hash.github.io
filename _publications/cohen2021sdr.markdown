---
layout: publication
title: 'SDR: Efficient Neural Re-ranking Using Succinct Document Representation'
authors: Nachshon Cohen, Amit Portnoy, Besnik Fetahu, Amir Ingber
conference: Arxiv
year: 2021
bibkey: cohen2021sdr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.02065'}]
tags: ["Memory Efficiency", "Quantization", "Re-Ranking"]
short_authors: Cohen et al.
---
BERT based ranking models have achieved superior performance on various
information retrieval tasks. However, the large number of parameters and
complex self-attention operation come at a significant latency overhead. To
remedy this, recent works propose late-interaction architectures, which allow
pre-computation of intermediate document representations, thus reducing the
runtime latency. Nonetheless, having solved the immediate latency issue, these
methods now introduce storage costs and network fetching latency, which limits
their adoption in real-life production systems.
  In this work, we propose the Succinct Document Representation (SDR) scheme
that computes highly compressed intermediate document representations,
mitigating the storage/network issue. Our approach first reduces the dimension
of token representations by encoding them using a novel autoencoder
architecture that uses the document's textual content in both the encoding and
decoding phases. After this token encoding step, we further reduce the size of
entire document representations using a modern quantization technique.
  Extensive evaluations on passage re-reranking on the MSMARCO dataset show
that compared to existing approaches using compressed document representations,
our method is highly efficient, achieving 4x-11.6x better compression rates for
the same ranking quality.