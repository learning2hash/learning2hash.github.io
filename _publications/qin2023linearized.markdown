---
layout: publication
title: Linearized Relative Positional Encoding
authors: Zhen Qin, Weixuan Sun, Kaiyue Lu, Hui Deng, Dongxu Li, Xiaodong Han, Yuchao
  Dai, Lingpeng Kong, Yiran Zhong
conference: Arxiv
year: 2023
bibkey: qin2023linearized
citations: 2
additional_links: [{name: Code, url: 'https://github.com/OpenNLPLab/Lrpe'}, {name: Paper,
    url: 'https://arxiv.org/abs/2307.09270'}]
tags: []
short_authors: Qin et al.
---
Relative positional encoding is widely used in vanilla and linear
transformers to represent positional information. However, existing encoding
methods of a vanilla transformer are not always directly applicable to a linear
transformer, because the latter requires a decomposition of the query and key
representations into separate kernel functions. Nevertheless, principles for
designing encoding methods suitable for linear transformers remain
understudied. In this work, we put together a variety of existing linear
relative positional encoding approaches under a canonical form and further
propose a family of linear relative positional encoding algorithms via unitary
transformation. Our formulation leads to a principled framework that can be
used to develop new relative positional encoding methods that preserve linear
space-time complexity. Equipped with different models, the proposed linearized
relative positional encoding (LRPE) family derives effective encoding for
various applications. Experiments show that compared with existing methods,
LRPE achieves state-of-the-art performance in language modeling, text
classification, and image classification. Meanwhile, it emphasizes a general
paradigm for designing broadly more relative positional encoding methods that
are applicable to linear transformers. The code is available at
https://github.com/OpenNLPLab/Lrpe.