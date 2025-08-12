---
layout: publication
title: 'Lex2sent: A Bagging Approach To Unsupervised Sentiment Analysis'
authors: Kai-Robin Lange, Jonas Rieger, Carsten Jentsch
conference: 20th Conference on Natural Language Processing (KONVENS 2024) 281-291
year: 2022
bibkey: lange2022lex2sent
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.13023'}]
tags: ["Unsupervised"]
short_authors: Kai-Robin Lange, Jonas Rieger, Carsten Jentsch
---
Unsupervised text classification, with its most common form being sentiment analysis, used to be performed by counting words in a text that were stored in a lexicon, which assigns each word to one class or as a neutral word. In recent years, these lexicon-based methods fell out of favor and were replaced by computationally demanding fine-tuning techniques for encoder-only models such as BERT and zero-shot classification using decoder-only models such as GPT-4. In this paper, we propose an alternative approach: Lex2Sent, which provides improvement over classic lexicon methods but does not require any GPU or external hardware. To classify texts, we train embedding models to determine the distances between document embeddings and the embeddings of the parts of a suitable lexicon. We employ resampling, which results in a bagging effect, boosting the performance of the classification. We show that our model outperforms lexica and provides a basis for a high performing few-shot fine-tuning approach in the task of binary sentiment analysis.