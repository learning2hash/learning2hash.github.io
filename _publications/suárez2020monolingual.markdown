---
layout: publication
title: A Monolingual Approach To Contextualized Word Embeddings For Mid-resource Languages
authors: "Pedro Javier Ortiz Su\xE1rez, Laurent Romary, Beno\xEEt Sagot"
conference: Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics
year: 2020
bibkey: "su\xE1rez2020monolingual"
citations: 154
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.06202'}]
tags: ["Evaluation"]
short_authors: "Pedro Javier Ortiz Su\xE1rez, Laurent Romary, Beno\xEEt Sagot"
---
We use the multilingual OSCAR corpus, extracted from Common Crawl via
language classification, filtering and cleaning, to train monolingual
contextualized word embeddings (ELMo) for five mid-resource languages. We then
compare the performance of OSCAR-based and Wikipedia-based ELMo embeddings for
these languages on the part-of-speech tagging and parsing tasks. We show that,
despite the noise in the Common-Crawl-based OSCAR data, embeddings trained on
OSCAR perform much better than monolingual embeddings trained on Wikipedia.
They actually equal or improve the current state of the art in tagging and
parsing for all five languages. In particular, they also improve over
multilingual Wikipedia-based contextual embeddings (multilingual BERT), which
almost always constitutes the previous state of the art, thereby showing that
the benefit of a larger, more diverse corpus surpasses the cross-lingual
benefit of multilingual embedding architectures.