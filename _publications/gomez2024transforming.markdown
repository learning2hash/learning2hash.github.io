---
layout: publication
title: Transforming Llms Into Cross-modal And Cross-lingual Retrieval Systems
authors: Frank Palma Gomez, Ramon Sanabria, Yun-Hsuan Sung, Daniel Cer, Siddharth
  Dalmia, Gustavo Hernandez Abrego
conference: Proceedings of the 21st International Conference on Spoken Language Translation
  (IWSLT 2024)
year: 2024
bibkey: gomez2024transforming
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01616'}]
tags: ["Evaluation"]
short_authors: Gomez et al.
---
Large language models (LLMs) are trained on text-only data that go far beyond
the languages with paired speech and text data. At the same time, Dual Encoder
(DE) based retrieval systems project queries and documents into the same
embedding space and have demonstrated their success in retrieval and bi-text
mining. To match speech and text in many languages, we propose using LLMs to
initialize multi-modal DE retrieval systems. Unlike traditional methods, our
system doesn't require speech data during LLM pre-training and can exploit
LLM's multilingual text understanding capabilities to match speech and text in
languages unseen during retrieval training. Our multi-modal LLM-based retrieval
system is capable of matching speech and text in 102 languages despite only
training on 21 languages. Our system outperforms previous systems trained
explicitly on all 102 languages. We achieve a 10% absolute improvement in
Recall@1 averaged across these languages. Additionally, our model demonstrates
cross-lingual speech and text matching, which is further enhanced by readily
available machine translation data.