---
layout: publication
title: 'Classbases At CASE-2022 Multilingual Protest Event Detection Tasks: Multilingual
  Protest News Detection And Automatically Replicating Manually Created Event Datasets'
authors: Peratham Wiriyathammabhum
conference: Arxiv
year: 2023
bibkey: wiriyathammabhum2023classbases
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.06617'}]
tags: ["Datasets"]
short_authors: Peratham Wiriyathammabhum
---
In this report, we describe our ClassBases submissions to a shared task on
multilingual protest event detection. For the multilingual protest news
detection, we participated in subtask-1, subtask-2, and subtask-4, which are
document classification, sentence classification, and token classification. In
subtask-1, we compare XLM-RoBERTa-base, mLUKE-base, and XLM-RoBERTa-large on
finetuning in a sequential classification setting. We always use a combination
of the training data from every language provided to train our multilingual
models. We found that larger models seem to work better and entity knowledge
helps but at a non-negligible cost. For subtask-2, we only submitted an
mLUKE-base system for sentence classification. For subtask-4, we only submitted
an XLM-RoBERTa-base for token classification system for sequence labeling. For
automatically replicating manually created event datasets, we participated in
COVID-related protest events from the New York Times news corpus. We created a
system to process the crawled data into a dataset of protest events.