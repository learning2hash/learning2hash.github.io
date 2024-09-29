---
layout: publication
title: PHPQ Pyramid Hybrid Pooling Quantization For Efficient Fine45;grained Image Retrieval
authors: Zeng Ziyun, Wang Jinpeng, Chen Bin, Dai Tao, Xia Shu-tao, Wang Zhi
conference: "Pattern Recognition Letters Volume"
year: 2021
bibkey: zeng2021phpq
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2109.05206"}
tags: ['CNN', 'Image Retrieval', 'Quantisation']
---
Deep hashing approaches including deep quantization and deep binary hashing have become a common solution to large45;scale image retrieval due to their high computation and storage efficiency. Most existing hashing methods cannot produce satisfactory results for fine45;grained retrieval because they usually adopt the outputs of the last CNN layer to generate binary codes. Since deeper layers tend to summarize visual clues e.g. texture into abstract semantics e.g. dogs and cats the feature produced by the last CNN layer is less effective in capturing subtle but discriminative visual details that mostly exist in shallow layers. To improve fine45;grained image hashing we propose Pyramid Hybrid Pooling Quantization (PHPQ). Specifically we propose a Pyramid Hybrid Pooling (PHP) module to capture and preserve fine45;grained semantic information from multi45;level features which emphasizes the subtle discrimination of different sub45;categories. Besides we propose a learnable quantization module with a partial codebook attention mechanism which helps to optimize the most relevant codewords and improves the quantization. Comprehensive experiments on two widely45;used public benchmarks i.e. CUB45;20045;2011 and Stanford Dogs demonstrate that PHPQ outperforms state45;of45;the45;art methods.
