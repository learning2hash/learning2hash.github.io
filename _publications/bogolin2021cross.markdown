---
layout: publication
title: Cross Modal Retrieval With Querybank Normalisation
authors: Simion-Vlad Bogolin, Ioana Croitoru, Hailin Jin, Yang Liu, Samuel Albanie
conference: Arxiv
year: 2021
bibkey: bogolin2021cross
citations: 4
additional_links: [{name: Code, url: 'https://vladbogo.github.io/QB-Norm/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2112.12777'}]
tags: [Evaluation, Datasets, Multimodal Retrieval, Scalability, Tools & Libraries]
short_authors: Bogolin et al.
---
Profiting from large-scale training datasets, advances in neural architecture
design and efficient inference, joint embeddings have become the dominant
approach for tackling cross-modal retrieval. In this work we first show that,
despite their effectiveness, state-of-the-art joint embeddings suffer
significantly from the longstanding "hubness problem" in which a small number
of gallery embeddings form the nearest neighbours of many queries. Drawing
inspiration from the NLP literature, we formulate a simple but effective
framework called Querybank Normalisation (QB-Norm) that re-normalises query
similarities to account for hubs in the embedding space. QB-Norm improves
retrieval performance without requiring retraining. Differently from prior
work, we show that QB-Norm works effectively without concurrent access to any
test set queries. Within the QB-Norm framework, we also propose a novel
similarity normalisation method, the Dynamic Inverted Softmax, that is
significantly more robust than existing approaches. We showcase QB-Norm across
a range of cross modal retrieval models and benchmarks where it consistently
enhances strong baselines beyond the state of the art. Code is available at
https://vladbogo.github.io/QB-Norm/.