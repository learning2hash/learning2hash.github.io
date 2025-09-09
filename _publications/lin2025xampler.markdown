---
layout: publication
title: 'XAMPLER: Learning To Retrieve Cross-lingual In-context Examples'
authors: "Peiqin Lin, Andr\xE9 F. T. Martins, Hinrich Sch\xFCtze"
conference: 'Findings of the Association for Computational Linguistics: NAACL 2025'
year: 2025
bibkey: lin2025xampler
citations: 0
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2405.05116'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "NAACL"]
short_authors: "Peiqin Lin, Andr\xE9 F. T. Martins, Hinrich Sch\xFCtze"
---
Recent studies indicate that leveraging off-the-shelf or fine-tuned
retrievers, capable of retrieving relevant in-context examples tailored to the
input query, enhances few-shot in-context learning of English. However,
adapting these methods to other languages, especially low-resource ones, poses
challenges due to the scarcity of cross-lingual retrievers and annotated data.
Thus, we introduce XAMPLER: Cross-Lingual Example Retrieval, a method tailored
to tackle the challenge of cross-lingual in-context learning using only
annotated English data. XAMPLER first trains a retriever based on Glot500, a
multilingual small language model, using positive and negative English examples
constructed from the predictions of a multilingual large language model, i.e.,
MaLA500. Leveraging the cross-lingual capacity of the retriever, it can
directly retrieve English examples as few-shot examples for in-context learning
of target languages. Experiments on two multilingual text classification
benchmarks, namely SIB200 with 176 languages and MasakhaNEWS with 16 languages,
demonstrate that XAMPLER substantially improves the in-context learning
performance across languages. Our code is available at
https://github.com/cisnlp/XAMPLER.