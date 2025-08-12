---
layout: publication
title: Representation Learning Of Image Schema
authors: "Fajrian Yunus, Chlo\xE9 Clavel, Catherine Pelachaud"
conference: Arxiv
year: 2022
bibkey: yunus2022representation
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.08256'}]
tags: ["Image Retrieval"]
short_authors: "Fajrian Yunus, Chlo\xE9 Clavel, Catherine Pelachaud"
---
Image schema is a recurrent pattern of reasoning where one entity is mapped
into another. Image schema is similar to conceptual metaphor and is also
related to metaphoric gesture. Our main goal is to generate metaphoric gestures
for an Embodied Conversational Agent.
  We propose a technique to learn the vector representation of image schemas.
As far as we are aware of, this is the first work which addresses that problem.
Our technique uses Ravenet et al's algorithm which we use to compute the image
schemas from the text input and also BERT and SenseBERT which we use as the
base word embedding technique to calculate the final vector representation of
the image schema. Our representation learning technique works by clustering:
word embedding vectors which belong to the same image schema should be
relatively closer to each other, and thus form a cluster.
  With the image schemas representable as vectors, it also becomes possible to
have a notion that some image schemas are closer or more similar to each other
than to the others because the distance between the vectors is a proxy of the
dissimilarity between the corresponding image schemas. Therefore, after
obtaining the vector representation of the image schemas, we calculate the
distances between those vectors. Based on these, we create visualizations to
illustrate the relative distances between the different image schemas.