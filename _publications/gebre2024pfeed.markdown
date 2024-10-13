---
layout: publication
title: Pfeed Generating Near Real-time Personalized Feeds Using Precomputed Embedding Similarities
authors: Gebre Binyam, Ranta Karoliina, Elzen Stef Van Den, Kuiper Ernst, Baars Thijs, Heskes Tom
conference: "Arxiv"
year: 2024
bibkey: gebre2024pfeed
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2402.16073"}
tags: ['ARXIV']
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
