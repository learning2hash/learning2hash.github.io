---
layout: publication
title: 'Inranker: Distilled Rankers For Zero-shot Information Retrieval'
authors: Thiago Laitz, Konstantinos Papakostas, Roberto Lotufo, Rodrigo Nogueira
conference: Arxiv
year: 2024
bibkey: laitz2024inranker
citations: 0
additional_links: [{name: Code, url: 'https://github.com/unicamp-dl/InRanker'}, {
    name: Paper, url: 'https://arxiv.org/abs/2401.06910'}]
tags: [Supervised, Re-ranking, Few-shot & Zero-shot]
short_authors: Laitz et al.
---
Despite multi-billion parameter neural rankers being common components of
state-of-the-art information retrieval pipelines, they are rarely used in
production due to the enormous amount of compute required for inference. In
this work, we propose a new method for distilling large rankers into their
smaller versions focusing on out-of-domain effectiveness. We introduce
InRanker, a version of monoT5 distilled from monoT5-3B with increased
effectiveness on out-of-domain scenarios. Our key insight is to use language
models and rerankers to generate as much as possible synthetic "in-domain"
training data, i.e., data that closely resembles the data that will be seen at
retrieval time. The pipeline consists of two distillation phases that do not
require additional user queries or manual annotations: (1) training on existing
supervised soft teacher labels, and (2) training on teacher soft labels for
synthetic queries generated using a large language model. Consequently, models
like monoT5-60M and monoT5-220M improved their effectiveness by using the
teacher's knowledge, despite being 50x and 13x smaller, respectively. Models
and code are available at https://github.com/unicamp-dl/InRanker.