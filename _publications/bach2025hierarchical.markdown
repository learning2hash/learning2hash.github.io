---
layout: publication
title: 'Hierarchical Patch Compression For Colpali: Efficient Multi-vector Document
  Retrieval With Dynamic Pruning And Quantization'
authors: Duong Bach
conference: Proceedings of the 17th International Joint Conference on Knowledge Discovery,
  Knowledge Engineering and Knowledge Management
year: 2025
bibkey: bach2025hierarchical
citations: 0
additional_links: [{name: Code, url: 'https://github.com/DngBack/HPC-ColPali'}, {
    name: Paper, url: 'https://arxiv.org/abs/2506.21601'}]
tags: ["Datasets", "Efficiency", "Quantization", "Similarity Search", "Text Retrieval"]
short_authors: Duong Bach
---
Multi-vector document retrieval systems, such as ColPali, excel in fine-grained matching for complex queries but incur significant storage and computational costs due to their reliance on high-dimensional patch embeddings and late-interaction scoring. To address these challenges, we propose HPC-ColPali, a Hierarchical Patch Compression framework that enhances the efficiency of ColPali while preserving its retrieval accuracy. Our approach integrates three innovative techniques: (1) K-Means quantization, which compresses patch embeddings into 1-byte centroid indices, achieving up to 32\(\times\) storage reduction; (2) attention-guided dynamic pruning, utilizing Vision-Language Model attention weights to retain only the top-\(p%\) most salient patches, reducing late-interaction computation by up to 60% with less than 2% nDCG@10 loss; and (3) optional binary encoding of centroid indices into \(b\)-bit strings (\(b=\lceillog_2 K\rceil\)), enabling rapid Hamming distance-based similarity search for resource-constrained environments. Evaluated on the ViDoRe and SEC-Filings datasets, HPC-ColPali achieves 30--50% lower query latency under HNSW indexing while maintaining high retrieval precision. When integrated into a Retrieval-Augmented Generation pipeline for legal summarization, it reduces hallucination rates by 30% and halves end-to-end latency. These advancements establish HPC-ColPali as a scalable and efficient solution for multi-vector document retrieval across diverse applications. Code is available at https://github.com/DngBack/HPC-ColPali.