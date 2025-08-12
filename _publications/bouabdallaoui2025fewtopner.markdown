---
layout: publication
title: 'Fewtopner: Integrating Few-shot Learning With Topic Modeling And Named Entity
  Recognition In A Multilingual Framework'
authors: Ibrahim Bouabdallaoui, Fatima Guerouate, Samya Bouhaddour, Chaimae Saadi,
  Mohammed Sbihi
conference: Arxiv
year: 2025
bibkey: bouabdallaoui2025fewtopner
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.02391'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bouabdallaoui et al.
---
We introduce FewTopNER, a novel framework that integrates few-shot named
entity recognition (NER) with topic-aware contextual modeling to address the
challenges of cross-lingual and low-resource scenarios. FewTopNER leverages a
shared multilingual encoder based on XLM-RoBERTa, augmented with
language-specific calibration mechanisms, to generate robust contextual
embeddings. The architecture comprises a prototype-based entity recognition
branch, employing BiLSTM and Conditional Random Fields for sequence labeling,
and a topic modeling branch that extracts document-level semantic features
through hybrid probabilistic and neural methods. A cross-task bridge
facilitates dynamic bidirectional attention and feature fusion between entity
and topic representations, thereby enhancing entity disambiguation by
incorporating global semantic context. Empirical evaluations on multilingual
benchmarks across English, French, Spanish, German, and Italian demonstrate
that FewTopNER significantly outperforms existing state-of-the-art few-shot NER
models. In particular, the framework achieves improvements of 2.5-4.0
percentage points in F1 score and exhibits enhanced topic coherence, as
measured by normalized pointwise mutual information. Ablation studies further
confirm the critical contributions of the shared encoder and cross-task
integration mechanisms to the overall performance. These results underscore the
efficacy of incorporating topic-aware context into few-shot NER and highlight
the potential of FewTopNER for robust cross-lingual applications in
low-resource settings.