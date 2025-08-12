---
layout: publication
title: 'FCSS: Fully Convolutional Self-similarity For Dense Semantic Correspondence'
authors: Seungryong Kim, Dongbo Min, Bumsub Ham, Sangryul Jeon, Stephen Lin, Kwanghoon
  Sohn
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: kim2017fcss
citations: 126
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.00926'}]
tags: ["CVPR"]
short_authors: Kim et al.
---
We present a descriptor, called fully convolutional self-similarity (FCSS),
for dense semantic correspondence. To robustly match points among different
instances within the same object class, we formulate FCSS using local
self-similarity (LSS) within a fully convolutional network. In contrast to
existing CNN-based descriptors, FCSS is inherently insensitive to intra-class
appearance variations because of its LSS-based structure, while maintaining the
precise localization ability of deep neural networks. The sampling patterns of
local structure and the self-similarity measure are jointly learned within the
proposed network in an end-to-end and multi-scale manner. As training data for
semantic correspondence is rather limited, we propose to leverage object
candidate priors provided in existing image datasets and also correspondence
consistency between object pairs to enable weakly-supervised learning.
Experiments demonstrate that FCSS outperforms conventional handcrafted
descriptors and CNN-based descriptors on various benchmarks.