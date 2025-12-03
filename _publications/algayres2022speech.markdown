---
layout: publication
title: Speech Sequence Embeddings Using Nearest Neighbors Contrastive Learning
authors: Robin Algayres, Adel Nabli, Benoit Sagot, Emmanuel Dupoux
conference: Interspeech 2022
year: 2022
bibkey: algayres2022speech
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.05148'}]
tags: ["Datasets", "Interspeech", "Self-Supervised", "Supervised", "Unsupervised"]
short_authors: Algayres et al.
---
We introduce a simple neural encoder architecture that can be trained using
an unsupervised contrastive learning objective which gets its positive samples
from data-augmented k-Nearest Neighbors search. We show that when built on top
of recent self-supervised audio representations, this method can be applied
iteratively and yield competitive SSE as evaluated on two tasks:
query-by-example of random sequences of speech, and spoken term discovery. On
both tasks our method pushes the state-of-the-art by a significant margin
across 5 different languages. Finally, we establish a benchmark on a
query-by-example task on the LibriSpeech dataset to monitor future improvements
in the field.