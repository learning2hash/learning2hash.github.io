---
layout: publication
title: Cover Detection Using Dominant Melody Embeddings
authors: Guillaume Doras, Geoffroy Peeters
conference: 20th International Society for Music Information Retrieval Conference
  Delft The Netherlands 2019
year: 2019
bibkey: doras2019cover
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.01824'}]
tags: ["Datasets", "Evaluation"]
short_authors: Guillaume Doras, Geoffroy Peeters
---
Automatic cover detection -- the task of finding in an audio database all the
covers of one or several query tracks -- has long been seen as a challenging
theoretical problem in the MIR community and as an acute practical problem for
authors and composers societies. Original algorithms proposed for this task
have proven their accuracy on small datasets, but are unable to scale up to
modern real-life audio corpora. On the other hand, faster approaches designed
to process thousands of pairwise comparisons resulted in lower accuracy, making
them unsuitable for practical use.
  In this work, we propose a neural network architecture that is trained to
represent each track as a single embedding vector. The computation burden is
therefore left to the embedding extraction -- that can be conducted offline and
stored, while the pairwise comparison task reduces to a simple Euclidean
distance computation. We further propose to extract each track's embedding out
of its dominant melody representation, obtained by another neural network
trained for this task. We then show that this architecture improves
state-of-the-art accuracy both on small and large datasets, and is able to
scale to query databases of thousands of tracks in a few seconds.