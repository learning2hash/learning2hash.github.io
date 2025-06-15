---
layout: publication
title: 'EHI: End-to-end Learning Of Hierarchical Index For Efficient Dense Retrieval'
authors: Ramnath Kumar et al.
conference: "Arxiv"
year: 2023
citations: 0
bibkey: kumar2023end
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2310.08891'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Unsupervised', 'Retrieval Models', 'Evaluation', 'Vector Indexing', 'Applications']
---
Dense embedding-based retrieval is widely used for semantic search and
ranking. However, conventional two-stage approaches, involving contrastive
embedding learning followed by approximate nearest neighbor search (ANNS), can
suffer from misalignment between these stages. This mismatch degrades retrieval
performance. We propose End-to-end Hierarchical Indexing (EHI), a novel method
that directly addresses this issue by jointly optimizing embedding generation
and ANNS structure. EHI leverages a dual encoder for embedding queries and
documents while simultaneously learning an inverted file index (IVF)-style tree
structure. To facilitate the effective learning of this discrete structure, EHI
introduces dense path embeddings that encodes the path traversed by queries and
documents within the tree. Extensive evaluations on standard benchmarks,
including MS MARCO (Dev set) and TREC DL19, demonstrate EHI's superiority over
traditional ANNS index. Under the same computational constraints, EHI
outperforms existing state-of-the-art methods by +1.45% in MRR@10 on MS MARCO
(Dev) and +8.2% in nDCG@10 on TREC DL19, highlighting the benefits of our
end-to-end approach.
