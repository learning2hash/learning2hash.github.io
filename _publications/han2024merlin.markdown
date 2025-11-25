---
layout: publication
title: 'MERLIN: Multimodal Embedding Refinement Via Llm-based Iterative Navigation
  For Text-video Retrieval-rerank Pipeline'
authors: Donghoon Han, Eunhwan Park, Gisang Lee, Adam Lee, Nojun Kwak
conference: 'Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing: Industry Track'
year: 2024
bibkey: han2024merlin
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.12508'}]
tags: ["EMNLP", "Evaluation", "Multimodal Retrieval", "Video Retrieval"]
short_authors: Han et al.
---
The rapid expansion of multimedia content has made accurately retrieving
relevant videos from large collections increasingly challenging. Recent
advancements in text-video retrieval have focused on cross-modal interactions,
large-scale foundation model training, and probabilistic modeling, yet often
neglect the crucial user perspective, leading to discrepancies between user
queries and the content retrieved. To address this, we introduce MERLIN
(Multimodal Embedding Refinement via LLM-based Iterative Navigation), a novel,
training-free pipeline that leverages Large Language Models (LLMs) for
iterative feedback learning. MERLIN refines query embeddings from a user
perspective, enhancing alignment between queries and video content through a
dynamic question answering process. Experimental results on datasets like
MSR-VTT, MSVD, and ActivityNet demonstrate that MERLIN substantially improves
Recall@1, outperforming existing systems and confirming the benefits of
integrating LLMs into multimodal retrieval systems for more responsive and
context-aware multimedia retrieval.