---
layout: publication
title: Shallow Cross-encoders For Low-latency Retrieval
authors: Aleksandr V. Petrov, Sean MacAvaney, Craig MacDonald
conference: Lecture Notes in Computer Science
year: 2024
bibkey: petrov2024shallow
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.20222'}]
tags: ["Efficiency", "Text Retrieval"]
short_authors: Aleksandr V. Petrov, Sean MacAvaney, Craig MacDonald
---
Transformer-based Cross-Encoders achieve state-of-the-art effectiveness in
text retrieval. However, Cross-Encoders based on large transformer models (such
as BERT or T5) are computationally expensive and allow for scoring only a small
number of documents within a reasonably small latency window. However, keeping
search latencies low is important for user satisfaction and energy usage. In
this paper, we show that weaker shallow transformer models (i.e., transformers
with a limited number of layers) actually perform better than full-scale models
when constrained to these practical low-latency settings since they can
estimate the relevance of more documents in the same time budget. We further
show that shallow transformers may benefit from the generalized Binary
Cross-Entropy (gBCE) training scheme, which has recently demonstrated success
for recommendation tasks. Our experiments with TREC Deep Learning passage
ranking query sets demonstrate significant improvements in shallow and
full-scale models in low-latency scenarios. For example, when the latency limit
is 25ms per query, MonoBERT-Large (a cross-encoder based on a full-scale BERT
model) is only able to achieve NDCG@10 of 0.431 on TREC DL 2019, while
TinyBERT-gBCE (a cross-encoder based on TinyBERT trained with gBCE) reaches
NDCG@10 of 0.652, a +51% gain over MonoBERT-Large. We also show that shallow
Cross-Encoders are effective even when used without a GPU (e.g., with CPU
inference, NDCG@10 decreases only by 3% compared to GPU inference with 50ms
latency), which makes Cross-Encoders practical to run even without specialized
hardware acceleration.