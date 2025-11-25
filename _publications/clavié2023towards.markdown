---
layout: publication
title: Towards Better Monolingual Japanese Retrievers With Multi-vector Models
authors: "Benjamin Clavi\xE9"
conference: Arxiv
year: 2023
bibkey: "clavi\xE92023towards"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.16144'}]
tags: ["Datasets", "Text Retrieval"]
short_authors: "Benjamin Clavi\xE9"
---
As language-specific training data tends to be sparsely available compared to
English, document retrieval in many languages has been largely relying on
multilingual models. In Japanese, the best performing deep-learning based
retrieval approaches rely on multilingual dense embedders, with Japanese-only
models lagging far behind. However, multilingual models require considerably
more compute and data to train and have higher computational and memory
requirements while often missing out on culturally-relevant information. In
this paper, we introduce JaColBERT, a family of multi-vector retrievers trained
on two magnitudes fewer data than their multilingual counterparts while
reaching competitive performance. Our strongest model largely outperform all
existing monolingual Japanese retrievers on all dataset, as well as the
strongest existing multilingual models on all out-of-domain tasks, highlighting
the need for specialised models able to handle linguistic specificities. These
results are achieved using a model with only 110 million parameters,
considerably smaller than all multilingual models, and using only a limited
Japanese-language. We believe our results show great promise to support
Japanese retrieval-enhanced application pipelines in a wide variety of domains.