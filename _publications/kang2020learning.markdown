---
layout: publication
title: Learning Multi-granular Quantized Embeddings For Large-vocab Categorical Features
  In Recommender Systems
authors: Wang-Cheng Kang, Derek Zhiyuan Cheng, Ting Chen, Xinyang Yi, Dong Lin, Lichan
  Hong, Ed H. Chi
conference: Companion Proceedings of the Web Conference 2020
year: 2020
bibkey: kang2020learning
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.08530'}]
tags: ["Datasets", "Evaluation", "Quantization", "Recommender Systems"]
short_authors: Kang et al.
---
Recommender system models often represent various sparse features like users,
items, and categorical features via embeddings. A standard approach is to map
each unique feature value to an embedding vector. The size of the produced
embedding table grows linearly with the size of the vocabulary. Therefore, a
large vocabulary inevitably leads to a gigantic embedding table, creating two
severe problems: (i) making model serving intractable in resource-constrained
environments; (ii) causing overfitting problems. In this paper, we seek to
learn highly compact embeddings for large-vocab sparse features in recommender
systems (recsys). First, we show that the novel Differentiable Product
Quantization (DPQ) approach can generalize to recsys problems. In addition, to
better handle the power-law data distribution commonly seen in recsys, we
propose a Multi-Granular Quantized Embeddings (MGQE) technique which learns
more compact embeddings for infrequent items. We seek to provide a new angle to
improve recommendation performance with compact model sizes. Extensive
experiments on three recommendation tasks and two datasets show that we can
achieve on par or better performance, with only ~20% of the original model
size.