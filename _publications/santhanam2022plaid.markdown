---
layout: publication
title: 'PLAID: An Efficient Engine For Late Interaction Retrieval'
authors: Keshav Santhanam, Omar Khattab, Christopher Potts, Matei Zaharia
conference: Arxiv
year: 2022
bibkey: santhanam2022plaid
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.09707'}]
tags: ["Efficiency", "Evaluation", "Scalability"]
short_authors: Santhanam et al.
---
Pre-trained language models are increasingly important components across
multiple information retrieval (IR) paradigms. Late interaction, introduced
with the ColBERT model and recently refined in ColBERTv2, is a popular paradigm
that holds state-of-the-art status across many benchmarks. To dramatically
speed up the search latency of late interaction, we introduce the
Performance-optimized Late Interaction Driver (PLAID). Without impacting
quality, PLAID swiftly eliminates low-scoring passages using a novel centroid
interaction mechanism that treats every passage as a lightweight bag of
centroids. PLAID uses centroid interaction as well as centroid pruning, a
mechanism for sparsifying the bag of centroids, within a highly-optimized
engine to reduce late interaction search latency by up to 7\(\times\) on a GPU
and 45\(\times\) on a CPU against vanilla ColBERTv2, while continuing to deliver
state-of-the-art retrieval quality. This allows the PLAID engine with ColBERTv2
to achieve latency of tens of milliseconds on a GPU and tens or just few
hundreds of milliseconds on a CPU at large scale, even at the largest scales we
evaluate with 140M passages.