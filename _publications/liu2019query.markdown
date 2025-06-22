---
layout: publication
title: Query-adaptive Hash Code Ranking For Large-scale Multi-view Visual Search
authors: Xianglong Liu, Lei Huang, Cheng Deng, Bo Lang, Dacheng Tao
conference: Arxiv
year: 2019
citations: 66
bibkey: liu2019query
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08623'}]
tags: [Applications, Quantization, ANN Search, Efficient Learning, Evaluation Metrics,
  Loss Functions, Hashing Methods]
---
Hash based nearest neighbor search has become attractive in many
applications. However, the quantization in hashing usually degenerates the
discriminative power when using Hamming distance ranking. Besides, for
large-scale visual search, existing hashing methods cannot directly support the
efficient search over the data with multiple sources, and while the literature
has shown that adaptively incorporating complementary information from diverse
sources or views can significantly boost the search performance. To address the
problems, this paper proposes a novel and generic approach to building multiple
hash tables with multiple views and generating fine-grained ranking results at
bitwise and tablewise levels. For each hash table, a query-adaptive bitwise
weighting is introduced to alleviate the quantization loss by simultaneously
exploiting the quality of hash functions and their complement for nearest
neighbor search. From the tablewise aspect, multiple hash tables are built for
different data views as a joint index, over which a query-specific rank fusion
is proposed to rerank all results from the bitwise ranking by diffusing in a
graph. Comprehensive experiments on image search over three well-known
benchmarks show that the proposed method achieves up to 17.11% and 20.28%
performance gains on single and multiple table search over state-of-the-art
methods.