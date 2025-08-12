---
layout: publication
title: Experiments On Paraphrase Identification Using Quora Question Pairs Dataset
authors: Andreas Chandra, Ruben Stefanus
conference: Arxiv
year: 2020
bibkey: chandra2020experiments
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.02648'}]
tags: ["Datasets", "Evaluation"]
short_authors: Andreas Chandra, Ruben Stefanus
---
We modeled the Quora question pairs dataset to identify a similar question.
The dataset that we use is provided by Quora. The task is a binary
classification. We tried several methods and algorithms and different approach
from previous works. For feature extraction, we used Bag of Words including
Count Vectorizer, and Term Frequency-Inverse Document Frequency with unigram
for XGBoost and CatBoost. Furthermore, we also experimented with WordPiece
tokenizer which improves the model performance significantly. We achieved up to
97 percent accuracy. Code and Dataset.