---
layout: publication
title: An Experimental Evaluation Of Japanese Tokenizers For Sentiment-based Text
  Classification
authors: Andre Rusli, Makoto Shishido
conference: Arxiv
year: 2024
bibkey: rusli2024experimental
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.17361'}]
tags: ["Evaluation"]
short_authors: Andre Rusli, Makoto Shishido
---
This study investigates the performance of three popular tokenization tools:
MeCab, Sudachi, and SentencePiece, when applied as a preprocessing step for
sentiment-based text classification of Japanese texts. Using Term
Frequency-Inverse Document Frequency (TF-IDF) vectorization, we evaluate two
traditional machine learning classifiers: Multinomial Naive Bayes and Logistic
Regression. The results reveal that Sudachi produces tokens closely aligned
with dictionary definitions, while MeCab and SentencePiece demonstrate faster
processing speeds. The combination of SentencePiece, TF-IDF, and Logistic
Regression outperforms the other alternatives in terms of classification
performance.