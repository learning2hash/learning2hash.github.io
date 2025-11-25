---
layout: publication
title: On The Rankability Of Visual Embeddings
authors: Ankit Sonthalia, Arnas Uselis, Seong Joon Oh
conference: Arxiv
year: 2025
bibkey: sonthalia2025on
citations: 0
additional_links: [{name: Code, url: 'https://github.com/aktsonthalia/rankable-vision-embeddings'},
  {name: Paper, url: 'https://arxiv.org/abs/2507.03683'}]
tags: ["Datasets", "Image Retrieval", "Similarity Search", "Unsupervised", "Vector Indexing"]
short_authors: Ankit Sonthalia, Arnas Uselis, Seong Joon Oh
---
We study whether visual embedding models capture continuous, ordinal attributes along linear directions, which we term _rank axes_. We define a model as _rankable_ for an attribute if projecting embeddings onto such an axis preserves the attribute's order. Across 7 popular encoders and 9 datasets with attributes like age, crowd count, head pose, aesthetics, and recency, we find that many embeddings are inherently rankable. Surprisingly, a small number of samples, or even just two extreme examples, often suffice to recover meaningful rank axes, without full-scale supervision. These findings open up new use cases for image ranking in vector databases and motivate further study into the structure and learning of rankable embeddings. Our code is available at https://github.com/aktsonthalia/rankable-vision-embeddings.