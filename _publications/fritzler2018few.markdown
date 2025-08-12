---
layout: publication
title: Few-shot Classification In Named Entity Recognition Task
authors: Alexander Fritzler, Varvara Logacheva, Maksim Kretov
conference: Proceedings of the 34th ACM/SIGAPP Symposium on Applied Computing
year: 2019
bibkey: fritzler2018few
citations: 90
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.06158'}]
tags: []
short_authors: Alexander Fritzler, Varvara Logacheva, Maksim Kretov
---
For many natural language processing (NLP) tasks the amount of annotated data
is limited. This urges a need to apply semi-supervised learning techniques,
such as transfer learning or meta-learning. In this work we tackle Named Entity
Recognition (NER) task using Prototypical Network - a metric learning
technique. It learns intermediate representations of words which cluster well
into named entity classes. This property of the model allows classifying words
with extremely limited number of training examples, and can potentially be used
as a zero-shot learning method. By coupling this technique with transfer
learning we achieve well-performing classifiers trained on only 20 instances of
a target class.