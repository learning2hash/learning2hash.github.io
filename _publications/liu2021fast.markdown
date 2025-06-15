---
layout: publication
title: 'FDDH: Fast Discriminative Discrete Hashing For Large-scale Cross-modal Retrieval'
authors: Xin Liu, Xingzhi Wang, Yiu-ming Cheung
conference: "IEEE Transactions on Neural Networks and Learning Systems 2021"
year: 2021
citations: 46
bibkey: liu2021fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2105.07128'}
  - {name: "Code", url: 'https://github.com/starxliu/FDDH'}
tags: ['Cross-Modal', 'Quantisation', 'Efficiency', 'Retrieval Models', 'Training Strategy', 'Shallow', 'Has Code', 'Quantization', 'Multi-Modal Hashing', 'Hashing']
---
Cross-modal hashing, favored for its effectiveness and efficiency, has
received wide attention to facilitating efficient retrieval across different
modalities. Nevertheless, most existing methods do not sufficiently exploit the
discriminative power of semantic information when learning the hash codes,
while often involving time-consuming training procedure for handling the
large-scale dataset. To tackle these issues, we formulate the learning of
similarity-preserving hash codes in terms of orthogonally rotating the semantic
data so as to minimize the quantization loss of mapping such data to hamming
space, and propose an efficient Fast Discriminative Discrete Hashing (FDDH)
approach for large-scale cross-modal retrieval. More specifically, FDDH
introduces an orthogonal basis to regress the targeted hash codes of training
examples to their corresponding semantic labels, and utilizes "-dragging
technique to provide provable large semantic margins. Accordingly, the
discriminative power of semantic information can be explicitly captured and
maximized. Moreover, an orthogonal transformation scheme is further proposed to
map the nonlinear embedding data into the semantic subspace, which can well
guarantee the semantic consistency between the data feature and its semantic
representation. Consequently, an efficient closed form solution is derived for
discriminative hash code learning, which is very computationally efficient. In
addition, an effective and stable online learning strategy is presented for
optimizing modality-specific projection functions, featuring adaptivity to
different training sizes and streaming data. The proposed FDDH approach
theoretically approximates the bi-Lipschitz continuity, runs sufficiently fast,
and also significantly improves the retrieval performance over the
state-of-the-art methods. The source code is released at:
https://github.com/starxliu/FDDH.
