---
layout: publication
title: 'FOBE And HOBE: First- And High-order Bipartite Embeddings'
authors: Justin Sybrandt, Ilya Safro
conference: Arxiv
year: 2019
bibkey: sybrandt2019fobe
citations: 8
additional_links: [{name: Code, url: 'http://sybrandt.com/2020/fobe_hobe'}, {name: Paper,
    url: 'https://arxiv.org/abs/1905.10953'}]
tags: ["Recommender Systems"]
short_authors: Justin Sybrandt, Ilya Safro
---
Typical graph embeddings may not capture type-specific bipartite graph
features that arise in such areas as recommender systems, data visualization,
and drug discovery. Machine learning methods utilized in these applications
would be better served with specialized embedding techniques. We propose two
embeddings for bipartite graphs that decompose edges into sets of indirect
relationships between node neighborhoods. When sampling higher-order
relationships, we reinforce similarities through algebraic distance on graphs.
We also introduce ensemble embeddings to combine both into a "best of both
worlds" embedding. The proposed methods are evaluated on link prediction and
recommendation tasks and compared with other state-of-the-art embeddings. While
being all highly beneficial in applications, we demonstrate that none of the
considered embeddings is clearly superior (in contrast to what is claimed in
many papers), and discuss the trade offs present among them. Reproducibility:
Our code, data sets, and results are all publicly available online at:
http://sybrandt.com/2020/fobe_hobe.