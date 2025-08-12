---
layout: publication
title: Semantic Similarity Prediction Is Better Than Other Semantic Similarity Measures
authors: Steffen Herbold
conference: Arxiv
year: 2023
bibkey: herbold2023semantic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.12697'}]
tags: ["Evaluation"]
short_authors: Steffen Herbold
---
Semantic similarity between natural language texts is typically measured
either by looking at the overlap between subsequences (e.g., BLEU) or by using
embeddings (e.g., BERTScore, S-BERT). Within this paper, we argue that when we
are only interested in measuring the semantic similarity, it is better to
directly predict the similarity using a fine-tuned model for such a task. Using
a fine-tuned model for the Semantic Textual Similarity Benchmark tasks (STS-B)
from the GLUE benchmark, we define the STSScore approach and show that the
resulting similarity is better aligned with our expectations on a robust
semantic similarity measure than other approaches.