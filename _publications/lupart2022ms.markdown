---
layout: publication
title: 'Ms-shift: An Analysis Of MS MARCO Distribution Shifts On Neural Retrieval'
authors: "Simon Lupart, Thibault Formal, St\xE9phane Clinchant"
conference: Arxiv
year: 2022
bibkey: lupart2022ms
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.02870'}]
tags: [Evaluation, Few-shot & Zero-shot, Datasets]
short_authors: "Simon Lupart, Thibault Formal, St\xE9phane Clinchant"
---
Pre-trained Language Models have recently emerged in Information Retrieval as
providing the backbone of a new generation of neural systems that outperform
traditional methods on a variety of tasks. However, it is still unclear to what
extent such approaches generalize in zero-shot conditions. The recent BEIR
benchmark provides partial answers to this question by comparing models on
datasets and tasks that differ from the training conditions. We aim to address
the same question by comparing models under more explicit distribution shifts.
To this end, we build three query-based distribution shifts within MS MARCO
(query-semantic, query-intent, query-length), which are used to evaluate the
three main families of neural retrievers based on BERT: sparse, dense, and
late-interaction -- as well as a monoBERT re-ranker. We further analyse the
performance drops between the train and test query distributions. In
particular, we experiment with two generalization indicators: the first one
based on train/test query vocabulary overlap, and the second based on
representations of a trained bi-encoder. Intuitively, those indicators verify
that the further away the test set is from the train one, the worse the drop in
performance. We also show that models respond differently to the shifts --
dense approaches being the most impacted. Overall, our study demonstrates that
it is possible to design more controllable distribution shifts as a tool to
better understand generalization of IR models. Finally, we release the MS MARCO
query subsets, which provide an additional resource to benchmark zero-shot
transfer in Information Retrieval.