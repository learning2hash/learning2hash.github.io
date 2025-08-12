---
layout: publication
title: Deep Span Representations For Named Entity Recognition
authors: Enwei Zhu, Yiyang Liu, Jinpeng Li
conference: 'Findings of the Association for Computational Linguistics: ACL 2023'
year: 2023
bibkey: zhu2022deep
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.04182'}]
tags: []
short_authors: Enwei Zhu, Yiyang Liu, Jinpeng Li
---
Span-based models are one of the most straightforward methods for named
entity recognition (NER). Existing span-based NER systems shallowly aggregate
the token representations to span representations. However, this typically
results in significant ineffectiveness for long-span entities, a coupling
between the representations of overlapping spans, and ultimately a performance
degradation. In this study, we propose DSpERT (Deep Span Encoder
Representations from Transformers), which comprises a standard Transformer and
a span Transformer. The latter uses low-layered span representations as
queries, and aggregates the token representations as keys and values, layer by
layer from bottom to top. Thus, DSpERT produces span representations of deep
semantics.
  With weight initialization from pretrained language models, DSpERT achieves
performance higher than or competitive with recent state-of-the-art systems on
eight NER benchmarks. Experimental results verify the importance of the depth
for span representations, and show that DSpERT performs particularly well on
long-span entities and nested structures. Further, the deep span
representations are well structured and easily separable in the feature space.