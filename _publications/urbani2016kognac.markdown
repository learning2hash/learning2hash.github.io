---
layout: publication
title: 'KOGNAC: Efficient Encoding Of Large Knowledge Graphs'
authors: Jacopo Urbani, Sourav Dutta, Sairam Gurajada, Gerhard Weikum
conference: Arxiv
year: 2016
bibkey: urbani2016kognac
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.04795'}]
tags: ["Efficiency", "Graph Based ANN", "Hashing Methods", "Memory Efficiency", "Scalability"]
short_authors: Urbani et al.
---
Many Web applications require efficient querying of large Knowledge Graphs
(KGs). We propose KOGNAC, a dictionary-encoding algorithm designed to improve
SPARQL querying with a judicious combination of statistical and semantic
techniques. In KOGNAC, frequent terms are detected with a frequency
approximation algorithm and encoded to maximise compression. Infrequent terms
are semantically grouped into ontological classes and encoded to increase data
locality. We evaluated KOGNAC in combination with state-of-the-art RDF engines,
and observed that it significantly improves SPARQL querying on KGs with up to
1B edges.