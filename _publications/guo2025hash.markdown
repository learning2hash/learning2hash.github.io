---
layout: publication
title: 'HASH-RAG: Bridging Deep Hashing With Retriever For Efficient, Fine Retrieval
  And Augmented Generation'
authors: Jinyu Guo, Xunlei Chen, Qiyang Xia, Zhaokun Wang, Jie Ou, Libo Qin, Shunyu
  Yao, Wenhong Tian
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: guo2025hash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.16133'}]
tags: ["Datasets", "Efficiency", "Hashing Methods", "Neural Hashing", "Similarity Search"]
short_authors: Guo et al.
---
Retrieval-Augmented Generation (RAG) encounters efficiency challenges when scaling to massive knowledge bases while preserving contextual relevance. We propose Hash-RAG, a framework that integrates deep hashing techniques with systematic optimizations to address these limitations. Our queries directly learn binary hash codes from knowledgebase code, eliminating intermediate feature extraction steps, and significantly reducing storage and computational overhead. Building upon this hash-based efficient retrieval framework, we establish the foundation for fine-grained chunking. Consequently, we design a Prompt-Guided Chunk-to-Context (PGCC) module that leverages retrieved hash-indexed propositions and their original document segments through prompt engineering to enhance the LLM's contextual awareness. Experimental evaluations on NQ, TriviaQA, and HotpotQA datasets demonstrate that our approach achieves a 90% reduction in retrieval time compared to conventional methods while maintaining considerate recall performance. Additionally, The proposed system outperforms retrieval/non-retrieval baselines by 1.4-4.3% in EM scores.