---
layout: publication
title: In Defense Of Cross-encoders For Zero-shot Retrieval
authors: Guilherme Rosa, Luiz Bonifacio, Vitor Jeronymo, Hugo Abonizio, Marzieh Fadaee,
  Roberto Lotufo, Rodrigo Nogueira
conference: Arxiv
year: 2022
bibkey: rosa2022in
citations: 6
additional_links: [{name: Code, url: 'https://github.com/guilhermemr04/scaling-zero-shot-retrieval.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2212.06121'}]
tags: [Evaluation, Few-shot & Zero-shot]
short_authors: Rosa et al.
---
Bi-encoders and cross-encoders are widely used in many state-of-the-art
retrieval pipelines. In this work we study the generalization ability of these
two types of architectures on a wide range of parameter count on both in-domain
and out-of-domain scenarios. We find that the number of parameters and early
query-document interactions of cross-encoders play a significant role in the
generalization ability of retrieval models. Our experiments show that
increasing model size results in marginal gains on in-domain test sets, but
much larger gains in new domains never seen during fine-tuning. Furthermore, we
show that cross-encoders largely outperform bi-encoders of similar size in
several tasks. In the BEIR benchmark, our largest cross-encoder surpasses a
state-of-the-art bi-encoder by more than 4 average points. Finally, we show
that using bi-encoders as first-stage retrievers provides no gains in
comparison to a simpler retriever such as BM25 on out-of-domain tasks. The code
is available at
https://github.com/guilhermemr04/scaling-zero-shot-retrieval.git