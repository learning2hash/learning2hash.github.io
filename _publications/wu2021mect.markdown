---
layout: publication
title: 'MECT: Multi-metadata Embedding Based Cross-transformer For Chinese Named Entity
  Recognition'
authors: Shuang Wu, Xiaoning Song, Zhenhua Feng
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: wu2021mect
citations: 103
additional_links: [{name: Code, url: 'https://github.com/CoderMusou/MECT4CNER'}, {
    name: Paper, url: 'https://arxiv.org/abs/2107.05418'}]
tags: []
short_authors: Shuang Wu, Xiaoning Song, Zhenhua Feng
---
Recently, word enhancement has become very popular for Chinese Named Entity
Recognition (NER), reducing segmentation errors and increasing the semantic and
boundary information of Chinese words. However, these methods tend to ignore
the information of the Chinese character structure after integrating the
lexical information. Chinese characters have evolved from pictographs since
ancient times, and their structure often reflects more information about the
characters. This paper presents a novel Multi-metadata Embedding based
Cross-Transformer (MECT) to improve the performance of Chinese NER by fusing
the structural information of Chinese characters. Specifically, we use
multi-metadata embedding in a two-stream Transformer to integrate Chinese
character features with the radical-level embedding. With the structural
characteristics of Chinese characters, MECT can better capture the semantic
information of Chinese characters for NER. The experimental results obtained on
several well-known benchmarking datasets demonstrate the merits and superiority
of the proposed MECT method.\footnote\{The source code of the proposed method is
publicly available at https://github.com/CoderMusou/MECT4CNER.