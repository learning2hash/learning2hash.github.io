---
layout: publication
title: Improving Zero-Shot Entity Retrieval through Effective Dense Representations
authors: Partalidou Eleni, Christou Despina, Tsoumakas Grigorios
conference: Proceedings of the 12th Hellenic Conference on Artificial Intelligence
year: 2022
bibkey: partalidou2022improving
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04156'}]
tags: [AAAI, Few Shot & Zero Shot]
---
Entity Linking (EL) seeks to align entity mentions in text to entries in a
knowledge-base and is usually comprised of two phases: candidate generation and
candidate ranking. While most methods focus on the latter, it is the candidate
generation phase that sets an upper bound to both time and accuracy performance
of the overall EL system. This work's contribution is a significant improvement
in candidate generation which thus raises the performance threshold for EL, by
generating candidates that include the gold entity in the least candidate set
(top-K). We propose a simple approach that efficiently embeds mention-entity
pairs in dense space through a BERT-based bi-encoder. Specifically, we extend
(Wu et al., 2020) by introducing a new pooling function and incorporating
entity type side-information. We achieve a new state-of-the-art 84.28% accuracy
on top-50 candidates on the Zeshel dataset, compared to the previous 82.06% on
the top-64 of (Wu et al., 2020). We report the results from extensive
experimentation using our proposed model on both seen and unseen entity
datasets. Our results suggest that our method could be a useful complement to
existing EL approaches.