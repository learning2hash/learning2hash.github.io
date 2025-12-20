---
layout: publication
title: Training Effective Neural Sentence Encoders From Automatically Mined Paraphrases
authors: "S\u0142awomir Dadas"
conference: 2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
year: 2022
bibkey: dadas2022training
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.12759'}]
tags: ["Datasets", "Evaluation"]
short_authors: "S\u0142awomir Dadas"
---
Sentence embeddings are commonly used in text clustering and semantic
retrieval tasks. State-of-the-art sentence representation methods are based on
artificial neural networks fine-tuned on large collections of manually labeled
sentence pairs. Sufficient amount of annotated data is available for
high-resource languages such as English or Chinese. In less popular languages,
multilingual models have to be used, which offer lower performance. In this
publication, we address this problem by proposing a method for training
effective language-specific sentence encoders without manually labeled data.
Our approach is to automatically construct a dataset of paraphrase pairs from
sentence-aligned bilingual text corpora. We then use the collected data to
fine-tune a Transformer language model with an additional recurrent pooling
layer. Our sentence encoder can be trained in less than a day on a single
graphics card, achieving high performance on a diverse set of sentence-level
tasks. We evaluate our method on eight linguistic tasks in Polish, comparing it
with the best available multilingual sentence encoders.