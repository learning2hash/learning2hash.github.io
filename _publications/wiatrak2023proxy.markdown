---
layout: publication
title: Proxy-based Zero-shot Entity Linking By Effective Candidate Retrieval
authors: MacIej Wiatrak, Eirini Arvaniti, Angus Brayne, Jonas Vetterle, Aaron Sim
conference: Arxiv
year: 2023
bibkey: wiatrak2023proxy
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.13318'}]
tags: ["Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Wiatrak et al.
---
A recent advancement in the domain of biomedical Entity Linking is the
development of powerful two-stage algorithms, an initial candidate retrieval
stage that generates a shortlist of entities for each mention, followed by a
candidate ranking stage. However, the effectiveness of both stages are
inextricably dependent on computationally expensive components. Specifically,
in candidate retrieval via dense representation retrieval it is important to
have hard negative samples, which require repeated forward passes and nearest
neighbour searches across the entire entity label set throughout training. In
this work, we show that pairing a proxy-based metric learning loss with an
adversarial regularizer provides an efficient alternative to hard negative
sampling in the candidate retrieval stage. In particular, we show competitive
performance on the recall@1 metric, thereby providing the option to leave out
the expensive candidate ranking step. Finally, we demonstrate how the model can
be used in a zero-shot setting to discover out of knowledge base biomedical
entities.