---
layout: publication
title: 'Word2bits - Quantized Word Vectors'
authors: Maximilian Lam
conference: "Arxiv"
year: 2018
citations: 27
bibkey: lam2018quantized
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1803.05651'}
tags: ['Cross-Modal', 'Quantisation', 'Training Strategy', 'Shallow', 'Quantization']
---
Word vectors require significant amounts of memory and storage, posing issues
to resource limited devices like mobile phones and GPUs. We show that high
quality quantized word vectors using 1-2 bits per parameter can be learned by
introducing a quantization function into Word2Vec. We furthermore show that
training with the quantization function acts as a regularizer. We train word
vectors on English Wikipedia (2017) and evaluate them on standard word
similarity and analogy tasks and on question answering (SQuAD). Our quantized
word vectors not only take 8-16x less space than full precision (32 bit) word
vectors but also outperform them on word similarity tasks and question
answering.
