---
layout: publication
title: 'Stop Pre-training: Adapt Visual-language Models To Unseen Languages'
authors: "Yasmine Karoui, R\xE9mi Lebret, Negar Foroutan, Karl Aberer"
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2023
bibkey: karoui2023stop
citations: 1
additional_links: [{name: Code, url: 'https://github.com/Yasminekaroui/CliCoTea.'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.16774'}]
tags: [Text Retrieval, Evaluation, Few-shot & Zero-shot, ACL]
short_authors: Karoui et al.
---
Vision-Language Pre-training (VLP) has advanced the performance of many
vision-language tasks, such as image-text retrieval, visual entailment, and
visual reasoning. The pre-training mostly utilizes lexical databases and image
queries in English. Previous work has demonstrated that the pre-training in
English does not transfer well to other languages in a zero-shot setting.
However, multilingual pre-trained language models (MPLM) have excelled at a
variety of single-modal language tasks. In this paper, we propose a simple yet
efficient approach to adapt VLP to unseen languages using MPLM. We utilize a
cross-lingual contextualized token embeddings alignment approach to train text
encoders for non-English languages. Our approach does not require image input
and primarily uses machine translation, eliminating the need for target
language data. Our evaluation across three distinct tasks (image-text
retrieval, visual entailment, and natural language visual reasoning)
demonstrates that this approach outperforms the state-of-the-art multilingual
vision-language models without requiring large parallel corpora. Our code is
available at https://github.com/Yasminekaroui/CliCoTea.