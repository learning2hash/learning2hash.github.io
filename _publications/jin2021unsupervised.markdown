---
layout: publication
title: "Unsupervised Discrete Hashing with Affinity Similarity"
authors: Sheng Jin, Hongxun Yao, Qin Zhou, Yao Liu, Jianqiang Huang, Xiansheng Hua
conference: TIP
year: 2021
bibkey: jin2021unsupervised
additional_links:
   - {name: "PDF", url: "https://ieeexplore.ieee.org/abstract/document/9467816"}
tags: ['TIP', 'Unsupervised']
---
In recent years, supervised hashing has been validated to greatly boost the performance of image retrieval. However, the label-hungry property requires massive label collection, making it intractable in practical scenarios. To liberate the model training procedure from laborious manual annotations, some unsupervised methods are proposed. However, the following two factors make unsupervised algorithms inferior to their supervised counterparts: (1) Without manually-defined labels, it is difficult to capture the semantic information across data, which is of crucial importance to guide robust binary code learning. (2) The widely adopted relaxation on binary constraints results in quantization error accumulation in the optimization procedure. To address the above-mentioned problems, in this paper, we propose a novel Unsupervised Discrete Hashing method (UDH). Specifically, to capture the semantic information, we propose a balanced graph-based semantic loss which explores the affinity priors in the original feature space. Then, we propose a novel self-supervised loss, termed orthogonal consistent loss, which can leverage semantic loss of instance and impose independence of codes. Moreover, by integrating the discrete optimization into the proposed unsupervised framework, the binary constraints are consistently preserved, alleviating the influence of quantization errors. Extensive experiments demonstrate that UDH outperforms state-of-the-art unsupervised methods for image retrieval.
