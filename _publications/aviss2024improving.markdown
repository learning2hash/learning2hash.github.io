---
layout: publication
title: Improving Embedding Accuracy For Document Retrieval Using Entity Relationship
  Maps And Model-aware Contrastive Sampling
authors: Thea Aviss
conference: Arxiv
year: 2024
bibkey: aviss2024improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.18105'}]
tags: [Text Retrieval, Evaluation]
short_authors: Thea Aviss
---
In this paper we present APEX-Embedding-7B (Advanced Processing for Epistemic
eXtraction), a 7-billion parameter decoder-only text Feature Extraction Model,
specifically designed for Document Retrieval-Augmented Generation (RAG) tasks.
Our approach employs two training techniques that yield an emergent improvement
in factual focus: (1) Pre-convergence interrupted fine-tuning using Structured
Entity Relationship Maps as training data input: designed to shift the model's
attention and create a bias towards factual content rather than semantic style
- this enhances plain text performance despite not being directly trained for
it; and (2) Model-Aware Contrastive Sampling, creating a balanced and evenly
distributed collation map of hard and soft negatives directly informed by the
base model's competency. This combined methodology yields significant
improvements, enhancing plain text query/document pair retrieval to achieve an
absolute rank@1 accuracy of 90.86% (an increase of 6.26% compared to the next
leading model) in our evaluation, and reducing training data input context size
by an average of 37.71% compared to plain text for both queries and document
texts. Based on our evaluations, our model establishes a new state-of-the-art
standard in text feature extraction for longer context document retrieval
tasks.