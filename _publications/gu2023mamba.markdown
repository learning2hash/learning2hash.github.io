---
layout: publication
title: Mamba Linear-time Sequence Modeling With Selective State Spaces
authors: Albert Gu, Tri Dao
conference: "Arxiv"
year: 2023
bibkey: gu2023mamba
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2312.00752v2"}
tags: ['ARXIV', 'Deep Learning', 'Supervised']
---
Foundation models now powering most of the exciting applications in deep learning are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention gated convolution and recurrent models and structured state space models (SSMs) have been developed to address Transformers computational inefficiency on long sequences but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning and make several improvements. First simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second even though this change prevents the use of efficient convolutions we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5(times) higher throughput than Transformers) and linear scaling in sequence length and its performance improves on real data up to million-length sequences. As a general sequence model backbone Mamba achieves state-of-the-art performance across several modalities such as language audio and genomics. On language modeling our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size both in pretraining and downstream evaluation.
