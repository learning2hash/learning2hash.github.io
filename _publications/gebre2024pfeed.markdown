---
layout: publication
title: 'Pfeed: Generating Near Real-time Personalized Feeds Using Precomputed Embedding
  Similarities'
authors: Binyam Gebre, Karoliina Ranta, Stef van Den Elzen, Ernst Kuiper, Thijs Baars,
  Tom Heskes
conference: Arxiv
year: 2024
bibkey: gebre2024pfeed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16073'}]
tags: [Recommender Systems, Efficiency]
short_authors: Gebre et al.
---
In personalized recommender systems, embeddings are often used to encode
customer actions and items, and retrieval is then performed in the embedding
space using approximate nearest neighbor search. However, this approach can
lead to two challenges: 1) user embeddings can restrict the diversity of
interests captured and 2) the need to keep them up-to-date requires an
expensive, real-time infrastructure. In this paper, we propose a method that
overcomes these challenges in a practical, industrial setting. The method
dynamically updates customer profiles and composes a feed every two minutes,
employing precomputed embeddings and their respective similarities. We tested
and deployed this method to personalise promotional items at Bol, one of the
largest e-commerce platforms of the Netherlands and Belgium. The method
enhanced customer engagement and experience, leading to a significant 4.9%
uplift in conversions.