---
layout: publication
title: 'Rag-visualrec: An Open Resource For Vision- And Text-enhanced Retrieval-augmented
  Generation In Recommendation'
authors: Ali Tourani, Fatemeh Nazary, Yashar Deldjoo
conference: Arxiv
year: 2025
bibkey: tourani2025rag
citations: 0
additional_links: [{name: Code, url: 'https://github.com/RecSys-lab/RAG-VisualRec'},
  {name: Paper, url: 'https://arxiv.org/abs/2506.20817'}]
tags: ["Evaluation", "Hybrid ANN Methods", "Re-Ranking", "Recommender Systems", "Tools & Libraries"]
short_authors: Ali Tourani, Fatemeh Nazary, Yashar Deldjoo
---
This paper addresses the challenge of developing multimodal recommender systems for the movie domain, where limited metadata (e.g., title, genre) often hinders the generation of robust recommendations. We introduce a resource that combines LLM-generated plot descriptions with trailer-derived visual embeddings in a unified pipeline supporting both Retrieval-Augmented Generation (RAG) and collaborative filtering. Central to our approach is a data augmentation step that transforms sparse metadata into richer textual signals, alongside fusion strategies (e.g., PCA, CCA) that integrate visual cues. Experimental evaluations demonstrate that CCA-based fusion significantly boosts recall compared to unimodal baselines, while an LLM-driven re-ranking step further improves NDCG, particularly in scenarios with limited textual data. By releasing this framework, we invite further exploration of multi-modal recommendation techniques tailored to cold-start, novelty-focused, and domain-specific settings. All code, data, and detailed documentation are publicly available at: https://github.com/RecSys-lab/RAG-VisualRec