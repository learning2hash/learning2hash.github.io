---
layout: publication
title: Leveraging Approximate Caching For Faster Retrieval-augmented Generation
authors: Bergman Shai, Ji Zhang, Kermarrec Anne-marie, Petrescu Diana, Pires Rafael,
  Randl Mathis, de Vos Martijn
conference: Proceedings of the 5th Workshop on Machine Learning and Systems
year: 2025
bibkey: bergman2025leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.05530'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Bergman et al.
---
Retrieval-augmented generation (RAG) enhances the reliability of large
language model (LLM) answers by integrating external knowledge. However, RAG
increases the end-to-end inference time since looking for relevant documents
from large vector databases is computationally expensive. To address this, we
introduce Proximity, an approximate key-value cache that optimizes the RAG
workflow by leveraging similarities in user queries. Instead of treating each
query independently, Proximity reuses previously retrieved documents when
similar queries appear, reducing reliance on expensive vector database lookups.
We evaluate Proximity on the MMLU and MedRAG benchmarks, demonstrating that it
significantly improves retrieval efficiency while maintaining response
accuracy. Proximity reduces retrieval latency by up to 59% while maintaining
accuracy and lowers the computational burden on the vector database. We also
experiment with different similarity thresholds and quantify the trade-off
between speed and recall. Our work shows that approximate caching is a viable
and effective strategy for optimizing RAG-based systems.