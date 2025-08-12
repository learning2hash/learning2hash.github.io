---
layout: publication
title: A Byte-sized Approach To Named Entity Recognition
authors: Emily Sheng, Prem Natarajan
conference: Arxiv
year: 2018
bibkey: sheng2018byte
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.08386'}]
tags: ["Datasets", "Evaluation"]
short_authors: Emily Sheng, Prem Natarajan
---
In biomedical literature, it is common for entity boundaries to not align
with word boundaries. Therefore, effective identification of entity spans
requires approaches capable of considering tokens that are smaller than words.
We introduce a novel, subword approach for named entity recognition (NER) that
uses byte-pair encodings (BPE) in combination with convolutional and recurrent
neural networks to produce byte-level tags of entities. We present experimental
results on several standard biomedical datasets, namely the BioCreative VI
Bio-ID, JNLPBA, and GENETAG datasets. We demonstrate competitive performance
while bypassing the specialized domain expertise needed to create biomedical
text tokenization rules.