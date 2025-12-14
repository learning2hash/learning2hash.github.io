---
layout: publication
title: Cold Start Similar Artists Ranking With Gravity-inspired Graph Autoencoders
authors: Guillaume Salha-Galvan, Romain Hennequin, Benjamin Chapus, Viet-Anh Tran,
  Michalis Vazirgiannis
conference: Fifteenth ACM Conference on Recommender Systems
year: 2021
bibkey: salhagalvan2021cold
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.01053'}]
tags: [Tools & Libraries, RecSys]
short_authors: Salha-Galvan et al.
---
On an artist's profile page, music streaming services frequently recommend a
ranked list of "similar artists" that fans also liked. However, implementing
such a feature is challenging for new artists, for which usage data on the
service (e.g. streams or likes) is not yet available. In this paper, we model
this cold start similar artists ranking problem as a link prediction task in a
directed and attributed graph, connecting artists to their top-k most similar
neighbors and incorporating side musical information. Then, we leverage a graph
autoencoder architecture to learn node embedding representations from this
graph, and to automatically rank the top-k most similar neighbors of new
artists using a gravity-inspired mechanism. We empirically show the flexibility
and the effectiveness of our framework, by addressing a real-world cold start
similar artists ranking problem on a global music streaming service. Along with
this paper, we also publicly release our source code as well as the industrial
graph data from our experiments.