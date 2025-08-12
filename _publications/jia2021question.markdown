---
layout: publication
title: Question Answering Infused Pre-training Of General-purpose Contextualized Representations
authors: Robin Jia, Mike Lewis, Luke Zettlemoyer
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: jia2021question
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.08190'}]
tags: []
short_authors: Robin Jia, Mike Lewis, Luke Zettlemoyer
---
We propose a pre-training objective based on question answering (QA) for
learning general-purpose contextual representations, motivated by the intuition
that the representation of a phrase in a passage should encode all questions
that the phrase can answer in context. To this end, we train a bi-encoder QA
model, which independently encodes passages and questions, to match the
predictions of a more accurate cross-encoder model on 80 million synthesized QA
pairs. By encoding QA-relevant information, the bi-encoder's token-level
representations are useful for non-QA downstream tasks without extensive (or in
some cases, any) fine-tuning. We show large improvements over both
RoBERTa-large and previous state-of-the-art results on zero-shot and few-shot
paraphrase detection on four datasets, few-shot named entity recognition on two
datasets, and zero-shot sentiment analysis on three datasets.