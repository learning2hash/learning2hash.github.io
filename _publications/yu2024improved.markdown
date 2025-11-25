---
layout: publication
title: Improved Learned Sparse Retrieval With Corpus-specific Vocabularies
authors: Puxuan Yu, Antonio Mallia, Matthias Petri
conference: Lecture Notes in Computer Science
year: 2024
bibkey: yu2024improved
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.06703'}]
tags: ["Efficiency", "Text Retrieval"]
short_authors: Puxuan Yu, Antonio Mallia, Matthias Petri
---
We explore leveraging corpus-specific vocabularies that improve both
efficiency and effectiveness of learned sparse retrieval systems. We find that
pre-training the underlying BERT model on the target corpus, specifically
targeting different vocabulary sizes incorporated into the document expansion
process, improves retrieval quality by up to 12% while in some scenarios
decreasing latency by up to 50%. Our experiments show that adopting
corpus-specific vocabulary and increasing vocabulary size decreases average
postings list length which in turn reduces latency. Ablation studies show
interesting interactions between custom vocabularies, document expansion
techniques, and sparsification objectives of sparse models. Both effectiveness
and efficiency improvements transfer to different retrieval approaches such as
uniCOIL and SPLADE and offer a simple yet effective approach to providing new
efficiency-effectiveness trade-offs for learned sparse retrieval systems.