---
layout: publication
title: 'Quicker ADC : Unlocking The Hidden Potential Of Product Quantization With
  SIMD'
authors: "Fabien Andr\xE9, Anne-Marie Kermarrec, Nicolas Le Scouarnec"
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: "andr\xE92018quicker"
citations: 18
additional_links: [{name: Code, url: 'http://github.com/nlescoua/faiss-quickeradc'},
  {name: Paper, url: 'https://arxiv.org/abs/1812.09162'}]
tags: ["Efficiency", "Evaluation", "Quantization", "Tools & Libraries", "Vector Indexing"]
short_authors: "Fabien Andr\xE9, Anne-Marie Kermarrec, Nicolas Le Scouarnec"
---
Efficient Nearest Neighbor (NN) search in high-dimensional spaces is a
foundation of many multimedia retrieval systems. A common approach is to rely
on Product Quantization, which allows the storage of large vector databases in
memory and efficient distance computations. Yet, implementations of nearest
neighbor search with Product Quantization have their performance limited by the
many memory accesses they perform. Following this observation, Andr\'e et al.
proposed Quick ADC with up to \(6\times\) faster implementations of \(m\times\{\}4\)
product quantizers (PQ) leveraging specific SIMD instructions. Quicker ADC is a
generalization of Quick ADC not limited to \(m\times\{\}4\) codes and supporting
AVX-512, the latest revision of SIMD instruction set. In doing so, Quicker ADC
faces the challenge of using efficiently 5,6 and 7-bit shuffles that do not
align to computer bytes or words. To this end, we introduce (i) irregular
product quantizers combining sub-quantizers of different granularity and (ii)
split tables allowing lookup tables larger than registers. We evaluate Quicker
ADC with multiple indexes including Inverted Multi-Indexes and IVF HNSW and
show that it outperforms the reference optimized implementations (i.e., FAISS
and polysemous codes) for numerous configurations. Finally, we release an
open-source fork of FAISS enhanced with Quicker ADC at
http://github.com/nlescoua/faiss-quickeradc.