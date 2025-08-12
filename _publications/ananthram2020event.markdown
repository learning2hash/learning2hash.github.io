---
layout: publication
title: Event Guided Denoising For Multilingual Relation Learning
authors: Amith Ananthram, Emily Allaway, Kathleen McKeown
conference: Proceedings of the 28th International Conference on Computational Linguistics
year: 2020
bibkey: ananthram2020event
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.02721'}]
tags: ["COLING", "Few Shot & Zero Shot"]
short_authors: Amith Ananthram, Emily Allaway, Kathleen McKeown
---
General purpose relation extraction has recently seen considerable gains in
part due to a massively data-intensive distant supervision technique from
Soares et al. (2019) that produces state-of-the-art results across many
benchmarks. In this work, we present a methodology for collecting high quality
training data for relation extraction from unlabeled text that achieves a
near-recreation of their zero-shot and few-shot results at a fraction of the
training cost. Our approach exploits the predictable distributional structure
of date-marked news articles to build a denoised corpus -- the extraction
process filters out low quality examples. We show that a smaller multilingual
encoder trained on this corpus performs comparably to the current
state-of-the-art (when both receive little to no fine-tuning) on few-shot and
standard relation benchmarks in English and Spanish despite using many fewer
examples (50k vs. 300mil+).