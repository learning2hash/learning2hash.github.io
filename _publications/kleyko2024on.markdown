---
layout: publication
title: On Design Choices In Similarity-preserving Sparse Randomized Embeddings
authors: Denis Kleyko, Dmitri A. Rachkovskij
conference: 2024 International Joint Conference on Neural Networks (IJCNN)
year: 2024
bibkey: kleyko2024on
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.14741'}]
tags: ["Locality-Sensitive-Hashing", "Similarity Search"]
short_authors: Denis Kleyko, Dmitri A. Rachkovskij
---
Expand & Sparsify is a principle that is observed in anatomically similar
neural circuits found in the mushroom body (insects) and the cerebellum
(mammals). Sensory data are projected randomly to much higher-dimensionality
(expand part) where only few the most strongly excited neurons are activated
(sparsify part). This principle has been leveraged to design a FlyHash
algorithm that forms similarity-preserving sparse embeddings, which have been
found useful for such tasks as novelty detection, pattern recognition, and
similarity search. Despite its simplicity, FlyHash has a number of design
choices to be set such as preprocessing of the input data, choice of
sparsifying activation function, and formation of the random projection matrix.
In this paper, we explore the effect of these choices on the performance of
similarity search with FlyHash embeddings. We find that the right combination
of design choices can lead to drastic difference in the search performance.