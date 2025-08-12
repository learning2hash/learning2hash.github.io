---
layout: publication
title: Abstractified Multi-instance Learning (AMIL) For Biomedical Relation Extraction
authors: William Hogan, Molly Huang, Yannis Katsis, Tyler Baldwin, Ho-Cheol Kim, Yoshiki
  Vazquez Baeza, Andrew Bartko, Chun-Nan Hsu
conference: 3rd Conference on Automated Knowledge Base Construction (2021)
year: 2021
bibkey: hogan2021abstractified
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.12501'}]
tags: ["Datasets", "Evaluation"]
short_authors: Hogan et al.
---
Relation extraction in the biomedical domain is a challenging task due to a
lack of labeled data and a long-tail distribution of fact triples. Many works
leverage distant supervision which automatically generates labeled data by
pairing a knowledge graph with raw textual data. Distant supervision produces
noisy labels and requires additional techniques, such as multi-instance
learning (MIL), to denoise the training signal. However, MIL requires multiple
instances of data and struggles with very long-tail datasets such as those
found in the biomedical domain. In this work, we propose a novel reformulation
of MIL for biomedical relation extraction that abstractifies biomedical
entities into their corresponding semantic types. By grouping entities by
types, we are better able to take advantage of the benefits of MIL and further
denoise the training signal. We show this reformulation, which we refer to as
abstractified multi-instance learning (AMIL), improves performance in
biomedical relationship extraction. We also propose a novel relationship
embedding architecture that further improves model performance.