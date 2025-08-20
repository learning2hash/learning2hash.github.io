---
layout: publication
title: 'Mucai At Wojoodner 2024: Arabic Named Entity Recognition With Nearest Neighbor
  Search'
authors: Ahmed Abdou, Tasneem Mohsen
conference: Arxiv
year: 2024
bibkey: abdou2024mucai
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.03652'}]
tags: [Similarity Search, Datasets]
short_authors: Ahmed Abdou, Tasneem Mohsen
---
Named Entity Recognition (NER) is a task in Natural Language Processing (NLP)
that aims to identify and classify entities in text into predefined categories.
However, when applied to Arabic data, NER encounters unique challenges stemming
from the language's rich morphological inflections, absence of capitalization
cues, and spelling variants, where a single word can comprise multiple
morphemes. In this paper, we introduce Arabic KNN-NER, our submission to the
Wojood NER Shared Task 2024 (ArabicNLP 2024). We have participated in the
shared sub-task 1 Flat NER. In this shared sub-task, we tackle fine-grained
flat-entity recognition for Arabic text, where we identify a single main entity
and possibly zero or multiple sub-entities for each word. Arabic KNN-NER
augments the probability distribution of a fine-tuned model with another label
probability distribution derived from performing a KNN search over the cached
training data. Our submission achieved 91% on the test set on the WojoodFine
dataset, placing Arabic KNN-NER on top of the leaderboard for the shared task.