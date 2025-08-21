---
layout: publication
title: 'From Context To Concept: Exploring Semantic Relationships In Music With Word2vec'
authors: Ching-Hua Chuan, Kat Agres, Dorien Herremans
conference: Neural Computing and Applications
year: 2018
bibkey: chuan2018context
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.12408'}]
tags: ["Evaluation", "Neural Hashing"]
short_authors: Ching-Hua Chuan, Kat Agres, Dorien Herremans
---
We explore the potential of a popular distributional semantics vector space
model, word2vec, for capturing meaningful relationships in ecological (complex
polyphonic) music. More precisely, the skip-gram version of word2vec is used to
model slices of music from a large corpus spanning eight musical genres. In
this newly learned vector space, a metric based on cosine distance is able to
distinguish between functional chord relationships, as well as harmonic
associations in the music. Evidence, based on cosine distance between
chord-pair vectors, suggests that an implicit circle-of-fifths exists in the
vector space. In addition, a comparison between pieces in different keys
reveals that key relationships are represented in word2vec space. These results
suggest that the newly learned embedded vector representation does in fact
capture tonal and harmonic characteristics of music, without receiving explicit
information about the musical content of the constituent slices. In order to
investigate whether proximity in the discovered space of embeddings is
indicative of `semantically-related' slices, we explore a music generation
task, by automatically replacing existing slices from a given piece of music
with new slices. We propose an algorithm to find substitute slices based on
spatial proximity and the pitch class distribution inferred in the chosen
subspace. The results indicate that the size of the subspace used has a
significant effect on whether slices belonging to the same key are selected. In
sum, the proposed word2vec model is able to learn music-vector embeddings that
capture meaningful tonal and harmonic relationships in music, thereby providing
a useful tool for exploring musical properties and comparisons across pieces,
as a potential input representation for deep learning models, and as a music
generation device.