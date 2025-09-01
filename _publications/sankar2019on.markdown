---
layout: publication
title: On-device Text Representations Robust To Misspellings Via Projections
authors: Chinnadhurai Sankar, Sujith Ravi, Zornitsa Kozareva
conference: 'Proceedings of the 16th Conference of the European Chapter of the Association
  for Computational Linguistics: Main Volume'
year: 2021
bibkey: sankar2019on
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05763'}]
tags: ["Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Chinnadhurai Sankar, Sujith Ravi, Zornitsa Kozareva
---
Recently, there has been a strong interest in developing natural language
applications that live on personal devices such as mobile phones, watches and
IoT with the objective to preserve user privacy and have low memory. Advances
in Locality-Sensitive Hashing (LSH)-based projection networks have demonstrated
state-of-the-art performance in various classification tasks without explicit
word (or word-piece) embedding lookup tables by computing on-the-fly text
representations. In this paper, we show that the projection based neural
classifiers are inherently robust to misspellings and perturbations of the
input text. We empirically demonstrate that the LSH projection based
classifiers are more robust to common misspellings compared to BiLSTMs (with
both word-piece & word-only tokenization) and fine-tuned BERT based methods.
When subject to misspelling attacks, LSH projection based classifiers had a
small average accuracy drop of 2.94% across multiple classifications tasks,
while the fine-tuned BERT model accuracy had a significant drop of 11.44%.