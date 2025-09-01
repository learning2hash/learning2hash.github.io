---
layout: publication
title: Man Is To Computer Programmer As Woman Is To Homemaker? Debiasing Word Embeddings
authors: Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, Adam Kalai
conference: Arxiv
year: 2016
bibkey: bolukbasi2016man
citations: 1434
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.06520'}]
tags: ["Evaluation", "Tools & Libraries"]
short_authors: Bolukbasi et al.
---
The blind application of machine learning runs the risk of amplifying biases
present in data. Such a danger is facing us with word embedding, a popular
framework to represent text data as vectors which has been used in many machine
learning and natural language processing tasks. We show that even word
embeddings trained on Google News articles exhibit female/male gender
stereotypes to a disturbing extent. This raises concerns because their
widespread use, as we describe, often tends to amplify these biases.
Geometrically, gender bias is first shown to be captured by a direction in the
word embedding. Second, gender neutral words are shown to be linearly separable
from gender definition words in the word embedding. Using these properties, we
provide a methodology for modifying an embedding to remove gender stereotypes,
such as the association between between the words receptionist and female,
while maintaining desired associations such as between the words queen and
female. We define metrics to quantify both direct and indirect gender biases in
embeddings, and develop algorithms to "debias" the embedding. Using
crowd-worker evaluation as well as standard benchmarks, we empirically
demonstrate that our algorithms significantly reduce gender bias in embeddings
while preserving the its useful properties such as the ability to cluster
related concepts and to solve analogy tasks. The resulting embeddings can be
used in applications without amplifying gender bias.