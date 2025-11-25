---
layout: publication
title: Fine-tuning The Swissbert Encoder Model For Embedding Sentences And Documents
authors: Juri Grosjean, Jannis Vamvas
conference: Arxiv
year: 2024
bibkey: grosjean2024fine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.07513'}]
tags: ["Self-Supervised", "Text Retrieval"]
short_authors: Juri Grosjean, Jannis Vamvas
---
Encoder models trained for the embedding of sentences or short documents have
proven useful for tasks such as semantic search and topic modeling. In this
paper, we present a version of the SwissBERT encoder model that we specifically
fine-tuned for this purpose. SwissBERT contains language adapters for the four
national languages of Switzerland -- German, French, Italian, and Romansh --
and has been pre-trained on a large number of news articles in those languages.
Using contrastive learning based on a subset of these articles, we trained a
fine-tuned version, which we call SentenceSwissBERT. Multilingual experiments
on document retrieval and text classification in a Switzerland-specific setting
show that SentenceSwissBERT surpasses the accuracy of the original SwissBERT
model and of a comparable baseline. The model is openly available for research
use.