---
layout: publication
title: 'MTVR: Multilingual Moment Retrieval In Videos'
authors: Jie Lei, Tamara L. Berg, Mohit Bansal
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 2: Short Papers)'
year: 2021
bibkey: lei2021mtvr
citations: 7
additional_links: [{name: Code, url: 'https://github.com/jayleicn/mTVRetrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2108.00061'}]
tags: []
short_authors: Jie Lei, Tamara L. Berg, Mohit Bansal
---
We introduce mTVR, a large-scale multilingual video moment retrieval dataset,
containing 218K English and Chinese queries from 21.8K TV show video clips. The
dataset is collected by extending the popular TVR dataset (in English) with
paired Chinese queries and subtitles. Compared to existing moment retrieval
datasets, mTVR is multilingual, larger, and comes with diverse annotations. We
further propose mXML, a multilingual moment retrieval model that learns and
operates on data from both languages, via encoder parameter sharing and
language neighborhood constraints. We demonstrate the effectiveness of mXML on
the newly collected MTVR dataset, where mXML outperforms strong monolingual
baselines while using fewer parameters. In addition, we also provide detailed
dataset analyses and model ablations. Data and code are publicly available at
https://github.com/jayleicn/mTVRetrieval