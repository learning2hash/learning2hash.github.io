---
layout: publication
title: 'Dblplink: An Entity Linker For The DBLP Scholarly Knowledge Graph'
authors: Debayan Banerjee, Arefa, Ricardo Usbeck, Chris Biemann
conference: Arxiv
year: 2023
bibkey: banerjee2023dblplink
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.07545'}]
tags: []
short_authors: Banerjee et al.
---
In this work, we present a web application named DBLPLink, which performs
entity linking over the DBLP scholarly knowledge graph. DBLPLink uses
text-to-text pre-trained language models, such as T5, to produce entity label
spans from an input text question. Entity candidates are fetched from a
database based on the labels, and an entity re-ranker sorts them based on
entity embeddings, such as TransE, DistMult and ComplEx. The results are
displayed so that users may compare and contrast the results between T5-small,
T5-base and the different KG embeddings used. The demo can be accessed at
https://ltdemos.informatik.uni-hamburg.de/dblplink/.