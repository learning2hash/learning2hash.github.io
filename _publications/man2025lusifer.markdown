---
layout: publication
title: 'LUSIFER: Language Universal Space Integration For Enhanced Multilingual Embeddings
  With Large Language Models'
authors: Man Hieu, Ngo Nghia Trung, Lai Viet Dac, Rossi Ryan A., Dernoncourt Franck,
  Nguyen Thien Huu
conference: Arxiv
year: 2025
bibkey: man2025lusifer
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.00874'}]
tags: ["Datasets", "Evaluation", "Few-shot & Zero-shot"]
short_authors: Man et al.
---
Recent advancements in large language models (LLMs) based embedding models
have established new state-of-the-art benchmarks for text embedding tasks,
particularly in dense vector-based retrieval. However, these models
predominantly focus on English, leaving multilingual embedding capabilities
largely unexplored. To address this limitation, we present LUSIFER, a novel
zero-shot approach that adapts LLM-based embedding models for multilingual
tasks without requiring multilingual supervision. LUSIFER's architecture
combines a multilingual encoder, serving as a language-universal learner, with
an LLM-based embedding model optimized for embedding-specific tasks. These
components are seamlessly integrated through a minimal set of trainable
parameters that act as a connector, effectively transferring the multilingual
encoder's language understanding capabilities to the specialized embedding
model. Additionally, to comprehensively evaluate multilingual embedding
performance, we introduce a new benchmark encompassing 5 primary embedding
tasks, 123 diverse datasets, and coverage across 14 languages. Extensive
experimental results demonstrate that LUSIFER significantly enhances the
multilingual performance across various embedding tasks, particularly for
medium and low-resource languages, without requiring explicit multilingual
training data.