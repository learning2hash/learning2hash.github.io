---
layout: publication
title: 'Bb_twtr At Semeval-2017 Task 4: Twitter Sentiment Analysis With Cnns And Lstms'
authors: Mathieu Cliche
conference: Proceedings of the 11th International Workshop on Semantic Evaluation
  (SemEval-2017)
year: 2017
bibkey: cliche2017bb_twtr
citations: 231
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.06125'}]
tags: []
short_authors: Mathieu Cliche
---
In this paper we describe our attempt at producing a state-of-the-art Twitter
sentiment classifier using Convolutional Neural Networks (CNNs) and Long Short
Term Memory (LSTMs) networks. Our system leverages a large amount of unlabeled
data to pre-train word embeddings. We then use a subset of the unlabeled data
to fine tune the embeddings using distant supervision. The final CNNs and LSTMs
are trained on the SemEval-2017 Twitter dataset where the embeddings are fined
tuned again. To boost performances we ensemble several CNNs and LSTMs together.
Our approach achieved first rank on all of the five English subtasks amongst 40
teams.