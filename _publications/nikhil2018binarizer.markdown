---
layout: publication
title: 'Binarizer At Semeval-2018 Task 3: Parsing Dependency And Deep Learning For
  Irony Detection'
authors: Nishant Nikhil, Muktabh Mayank Srivastava
conference: Proceedings of The 12th International Workshop on Semantic Evaluation
year: 2018
bibkey: nikhil2018binarizer
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.01112'}]
tags: []
short_authors: Nishant Nikhil, Muktabh Mayank Srivastava
---
In this paper, we describe the system submitted for the SemEval 2018 Task 3
(Irony detection in English tweets) Subtask A by the team Binarizer. Irony
detection is a key task for many natural language processing works. Our method
treats ironical tweets to consist of smaller parts containing different
emotions. We break down tweets into separate phrases using a dependency parser.
We then embed those phrases using an LSTM-based neural network model which is
pre-trained to predict emoticons for tweets. Finally, we train a
fully-connected network to achieve classification.