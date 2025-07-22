---
layout: publication
title: Enhancing Lexicon-based Text Embeddings With Large Language Models
authors: Lei Yibin, Shen Tao, Cao Yu, Yates Andrew
conference: Arxiv
year: 2025
bibkey: lei2025enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.09749'}]
tags: ["Evaluation"]
short_authors: Lei et al.
---
Recent large language models (LLMs) have demonstrated exceptional performance
on general-purpose text embedding tasks. While dense embeddings have dominated
related research, we introduce the first Lexicon-based EmbeddiNgS (LENS)
leveraging LLMs that achieve competitive performance on these tasks. Regarding
the inherent tokenization redundancy issue and unidirectional attention
limitations in traditional causal LLMs, LENS consolidates the vocabulary space
through token embedding clustering, and investigates bidirectional attention
and various pooling strategies. Specifically, LENS simplifies lexicon matching
by assigning each dimension to a specific token cluster, where semantically
similar tokens are grouped together, and unlocking the full potential of LLMs
through bidirectional attention. Extensive experiments demonstrate that LENS
outperforms dense embeddings on the Massive Text Embedding Benchmark (MTEB),
delivering compact feature representations that match the sizes of dense
counterparts. Notably, combining LENSE with dense embeddings achieves
state-of-the-art performance on the retrieval subset of MTEB (i.e. BEIR).