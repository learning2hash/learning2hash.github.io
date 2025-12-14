---
layout: publication
title: Flexible Retrieval With NMSLIB And Flexneuart
authors: Leonid Boytsov, Eric Nyberg
conference: Proceedings of Second Workshop for NLP Open Source Software (NLP-OSS)
year: 2020
bibkey: boytsov2020flexible
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.14848'}]
tags: [Tree-based ANN, Tools & Libraries, Re-ranking, Hybrid ANN Methods]
short_authors: Leonid Boytsov, Eric Nyberg
---
Our objective is to introduce to the NLP community an existing k-NN search
library NMSLIB, a new retrieval toolkit FlexNeuART, as well as their
integration capabilities. NMSLIB, while being one the fastest k-NN search
libraries, is quite generic and supports a variety of distance/similarity
functions. Because the library relies on the distance-based structure-agnostic
algorithms, it can be further extended by adding new distances. FlexNeuART is a
modular, extendible and flexible toolkit for candidate generation in IR and QA
applications, which supports mixing of classic and neural ranking signals.
FlexNeuART can efficiently retrieve mixed dense and sparse representations
(with weights learned from training data), which is achieved by extending
NMSLIB. In that, other retrieval systems work with purely sparse
representations (e.g., Lucene), purely dense representations (e.g., FAISS and
Annoy), or only perform mixing at the re-ranking stage.