---
layout: publication
title: 'Retrieve Fast, Rerank Smart: Cooperative And Joint Approaches For Improved
  Cross-modal Retrieval'
authors: "Gregor Geigle, Jonas Pfeiffer, Nils Reimers, Ivan Vuli\u0107, Iryna Gurevych"
conference: Transactions of the Association for Computational Linguistics
year: 2022
bibkey: geigle2021retrieve
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.11920'}]
tags: ["Efficiency", "Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Re-Ranking", "Similarity Search", "TACL", "Tools & Libraries"]
short_authors: Geigle et al.
---
Current state-of-the-art approaches to cross-modal retrieval process text and
visual input jointly, relying on Transformer-based architectures with
cross-attention mechanisms that attend over all words and objects in an image.
While offering unmatched retrieval performance, such models: 1) are typically
pretrained from scratch and thus less scalable, 2) suffer from huge retrieval
latency and inefficiency issues, which makes them impractical in realistic
applications. To address these crucial gaps towards both improved and efficient
cross-modal retrieval, we propose a novel fine-tuning framework that turns any
pretrained text-image multi-modal model into an efficient retrieval model. The
framework is based on a cooperative retrieve-and-rerank approach which
combines: 1) twin networks (i.e., a bi-encoder) to separately encode all items
of a corpus, enabling efficient initial retrieval, and 2) a cross-encoder
component for a more nuanced (i.e., smarter) ranking of the retrieved small set
of items. We also propose to jointly fine-tune the two components with shared
weights, yielding a more parameter-efficient model. Our experiments on a series
of standard cross-modal retrieval benchmarks in monolingual, multilingual, and
zero-shot setups, demonstrate improved accuracy and huge efficiency benefits
over the state-of-the-art cross-encoders.