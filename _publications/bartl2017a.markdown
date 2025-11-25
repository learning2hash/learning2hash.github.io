---
layout: publication
title: A Retrieval-based Dialogue System Utilizing Utterance And Context Embeddings
authors: Alexander Bartl, Gerasimos Spanakis
conference: 2017 16th IEEE International Conference on Machine Learning and Applications
  (ICMLA)
year: 2017
bibkey: bartl2017a
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.05780'}]
tags: ["Datasets", "Evaluation", "ICML", "Locality-Sensitive-Hashing"]
short_authors: Alexander Bartl, Gerasimos Spanakis
---
Finding semantically rich and computer-understandable representations for
textual dialogues, utterances and words is crucial for dialogue systems (or
conversational agents), as their performance mostly depends on understanding
the context of conversations. Recent research aims at finding distributed
vector representations (embeddings) for words, such that semantically similar
words are relatively close within the vector-space. Encoding the "meaning" of
text into vectors is a current trend, and text can range from words, phrases
and documents to actual human-to-human conversations. In recent research
approaches, responses have been generated utilizing a decoder architecture,
given the vector representation of the current conversation. In this paper, the
utilization of embeddings for answer retrieval is explored by using
Locality-Sensitive Hashing Forest (LSH Forest), an Approximate Nearest Neighbor
(ANN) model, to find similar conversations in a corpus and rank possible
candidates. Experimental results on the well-known Ubuntu Corpus (in English)
and a customer service chat dataset (in Dutch) show that, in combination with a
candidate selection method, retrieval-based approaches outperform generative
ones and reveal promising future research directions towards the usability of
such a system.