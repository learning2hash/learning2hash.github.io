---
layout: publication
title: Cross-lingual Training With Dense Retrieval For Document Retrieval
authors: Peng Shi, Rui Zhang, He Bai, Jimmy Lin
conference: Arxiv
year: 2021
bibkey: shi2021cross
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.01628'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Supervised", "Text Retrieval"]
short_authors: Shi et al.
---
Dense retrieval has shown great success in passage ranking in English.
However, its effectiveness in document retrieval for non-English languages
remains unexplored due to the limitation in training resources. In this work,
we explore different transfer techniques for document ranking from English
annotations to multiple non-English languages. Our experiments on the test
collections in six languages (Chinese, Arabic, French, Hindi, Bengali, Spanish)
from diverse language families reveal that zero-shot model-based transfer using
mBERT improves the search quality in non-English mono-lingual retrieval. Also,
we find that weakly-supervised target language transfer yields competitive
performances against the generation-based target language transfer that
requires external translators and query generators.