---
layout: publication
title: Deep Active Learning For Named Entity Recognition
authors: Yanyao Shen, Hyokun Yun, Zachary C. Lipton, Yakov Kronrod, Animashree Anandkumar
conference: Proceedings of the 2nd Workshop on Representation Learning for NLP
year: 2017
bibkey: shen2017deep
citations: 366
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05928'}]
tags: []
short_authors: Shen et al.
---
Deep learning has yielded state-of-the-art performance on many natural
language processing tasks including named entity recognition (NER). However,
this typically requires large amounts of labeled data. In this work, we
demonstrate that the amount of labeled training data can be drastically reduced
when deep learning is combined with active learning. While active learning is
sample-efficient, it can be computationally expensive since it requires
iterative retraining. To speed this up, we introduce a lightweight architecture
for NER, viz., the CNN-CNN-LSTM model consisting of convolutional character and
word encoders and a long short term memory (LSTM) tag decoder. The model
achieves nearly state-of-the-art performance on standard datasets for the task
while being computationally much more efficient than best performing models. We
carry out incremental active learning, during the training process, and are
able to nearly match state-of-the-art performance with just 25% of the
original training data.