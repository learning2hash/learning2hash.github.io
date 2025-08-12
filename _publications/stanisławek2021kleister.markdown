---
layout: publication
title: 'Kleister: Key Information Extraction Datasets Involving Long Documents With
  Complex Layouts'
authors: "Tomasz Stanis\u0142awek, Filip Grali\u0144ski, Anna Wr\xF3blewska, Dawid\
  \ Lipi\u0144ski, Agnieszka Kaliska, Paulina Rosalska, Bartosz Topolski, Przemys\u0142\
  aw Biecek"
conference: Lecture Notes in Computer Science
year: 2021
bibkey: "stanis\u0142awek2021kleister"
citations: 49
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.05796'}]
tags: ["Datasets"]
short_authors: "Stanis\u0142awek et al."
---
The relevance of the Key Information Extraction (KIE) task is increasingly
important in natural language processing problems. But there are still only a
few well-defined problems that serve as benchmarks for solutions in this area.
To bridge this gap, we introduce two new datasets (Kleister NDA and Kleister
Charity). They involve a mix of scanned and born-digital long formal
English-language documents. In these datasets, an NLP system is expected to
find or infer various types of entities by employing both textual and
structural layout features. The Kleister Charity dataset consists of 2,788
annual financial reports of charity organizations, with 61,643 unique pages and
21,612 entities to extract. The Kleister NDA dataset has 540 Non-disclosure
Agreements, with 3,229 unique pages and 2,160 entities to extract. We provide
several state-of-the-art baseline systems from the KIE domain (Flair, BERT,
RoBERTa, LayoutLM, LAMBERT), which show that our datasets pose a strong
challenge to existing models. The best model achieved an 81.77% and an 83.57%
F1-score on respectively the Kleister NDA and the Kleister Charity datasets. We
share the datasets to encourage progress on more in-depth and complex
information extraction tasks.