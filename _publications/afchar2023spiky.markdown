---
layout: publication
title: Of Spiky Svds And Music Recommendation
authors: Darius Afchar, Romain Hennequin, Vincent Guigue
conference: Proceedings of the 17th ACM Conference on Recommender Systems
year: 2023
bibkey: afchar2023spiky
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.01212'}]
tags: ["Datasets", "Recommender Systems"]
short_authors: Darius Afchar, Romain Hennequin, Vincent Guigue
---
The truncated singular value decomposition is a widely used methodology in
music recommendation for direct similar-item retrieval or embedding musical
items for downstream tasks. This paper investigates a curious effect that we
show naturally occurring on many recommendation datasets: spiking formations in
the embedding space. We first propose a metric to quantify this spiking
organization's strength, then mathematically prove its origin tied to
underlying communities of items of varying internal popularity. With this
new-found theoretical understanding, we finally open the topic with an
industrial use case of estimating how music embeddings' top-k similar items
will change over time under the addition of data.