---
layout: publication
title: Sequence-level Semantic Representation Fusion For Recommender Systems
authors: Lanling Xu, Zhen Tian, Bingqian Li, Junjie Zhang, Jinpeng Wang, Mingchen
  Cai, Wayne Xin Zhao
conference: Proceedings of the 33rd ACM International Conference on Information and
  Knowledge Management
year: 2024
bibkey: xu2024sequence
citations: 4
additional_links: [{name: Code, url: 'https://github.com/RUCAIBox/TedRec\'}, {name: Paper,
    url: 'https://arxiv.org/abs/2402.18166'}]
tags: ["CIKM", "Recommender Systems"]
short_authors: Xu et al.
---
With the rapid development of recommender systems, there is increasing side
information that can be employed to improve the recommendation performance.
Specially, we focus on the utilization of the associated *textual data* of
items (eg product title) and study how text features can be effectively fused
with ID features in sequential recommendation. However, there exists distinct
data characteristics for the two kinds of item features, making a direct fusion
method (eg adding text and ID embeddings as item representation) become less
effective. To address this issue, we propose a novel \{\ul *Te*\}xt-I\{\ul
*D*\} semantic fusion approach for sequential \{\ul *Rec*\}ommendation,
namely \textbf\{\our\}. The core idea of our approach is to conduct a
sequence-level semantic fusion approach by better integrating global contexts.
The key strategy lies in that we transform the text embeddings and ID
embeddings by Fourier Transform from *time domain* to *frequency
domain*. In the frequency domain, the global sequential characteristics of the
original sequences are inherently aggregated into the transformed
representations, so that we can employ simple multiplicative operations to
effectively fuse the two kinds of item features. Our fusion approach can be
proved to have the same effects of contextual convolution, so as to achieving
sequence-level semantic fusion. In order to further improve the fusion
performance, we propose to enhance the discriminability of the text embeddings
from the text encoder, by adaptively injecting positional information via a
mixture-of-experts~(MoE) modulation method. Our implementation is available at
this repository: \textcolor\{magenta\}\{https://github.com/RUCAIBox/TedRec\}.