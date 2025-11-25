---
layout: publication
title: Cross-lingual Paraphrase Identification
authors: Inessa Fedorova, Aleksei Musatow
conference: Arxiv
year: 2024
bibkey: fedorova2024cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.15066'}]
tags: ["Datasets", "Evaluation", "Similarity Search"]
short_authors: Inessa Fedorova, Aleksei Musatow
---
The paraphrase identification task involves measuring semantic similarity
between two short sentences. It is a tricky task, and multilingual paraphrase
identification is even more challenging. In this work, we train a bi-encoder
model in a contrastive manner to detect hard paraphrases across multiple
languages. This approach allows us to use model-produced embeddings for various
tasks, such as semantic search. We evaluate our model on downstream tasks and
also assess embedding space quality. Our performance is comparable to
state-of-the-art cross-encoders, with only a minimal relative drop of 7-10% on
the chosen dataset, while keeping decent quality of embeddings.