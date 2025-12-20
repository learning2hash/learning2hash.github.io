---
layout: publication
title: 'Loss In Translation: Learning Bilingual Word Mapping With A Retrieval Criterion'
authors: Armand Joulin, Piotr Bojanowski, Tomas Mikolov, Herve Jegou, Edouard Grave
conference: Proceedings of the 2018 Conference on Empirical Methods in Natural Language
  Processing
year: 2018
bibkey: joulin2018loss
citations: 339
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.07745'}]
tags: ["EMNLP", "Evaluation"]
short_authors: Joulin et al.
---
Continuous word representations learned separately on distinct languages can
be aligned so that their words become comparable in a common space. Existing
works typically solve a least-square regression problem to learn a rotation
aligning a small bilingual lexicon, and use a retrieval criterion for
inference. In this paper, we propose an unified formulation that directly
optimizes a retrieval criterion in an end-to-end fashion. Our experiments on
standard benchmarks show that our approach outperforms the state of the art on
word translation, with the biggest improvements observed for distant language
pairs such as English-Chinese.