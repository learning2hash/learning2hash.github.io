---
layout: publication
title: Generating Harder Cross-document Event Coreference Resolution Datasets Using
  Metaphoric Paraphrasing
authors: Shafiuddin Rehan Ahmed, Zhiyong Eric Wang, George Arthur Baker, Kevin Stowe,
  James H. Martin
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2024
bibkey: ahmed2024generating
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ahmeshaf/llms_coref'}, {
    name: Paper, url: 'https://arxiv.org/abs/2407.11988'}]
tags: ["Datasets"]
short_authors: Ahmed et al.
---
The most popular Cross-Document Event Coreference Resolution (CDEC) datasets
fail to convey the true difficulty of the task, due to the lack of lexical
diversity between coreferring event triggers (words or phrases that refer to an
event). Furthermore, there is a dearth of event datasets for figurative
language, limiting a crucial avenue of research in event comprehension. We
address these two issues by introducing ECB+META, a lexically rich variant of
Event Coref Bank Plus (ECB+) for CDEC on symbolic and metaphoric language. We
use ChatGPT as a tool for the metaphoric transformation of sentences in the
documents of ECB+, then tag the original event triggers in the transformed
sentences in a semi-automated manner. In this way, we avoid the re-annotation
of expensive coreference links. We present results that show existing methods
that work well on ECB+ struggle with ECB+META, thereby paving the way for CDEC
research on a much more challenging dataset. Code/data:
https://github.com/ahmeshaf/llms_coref