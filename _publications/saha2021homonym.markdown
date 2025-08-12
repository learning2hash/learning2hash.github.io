---
layout: publication
title: Homonym Identification Using BERT -- Using A Clustering Approach
authors: Rohan Saha
conference: Arxiv
year: 2021
bibkey: saha2021homonym
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.02398'}]
tags: ["Text Retrieval", "Transformer Based ANN"]
short_authors: Rohan Saha
---
Homonym identification is important for WSD that require coarse-grained
partitions of senses. The goal of this project is to determine whether
contextual information is sufficient for identifying a homonymous word. To
capture the context, BERT embeddings are used as opposed to Word2Vec, which
conflates senses into one vector. SemCor is leveraged to retrieve the
embeddings. Various clustering algorithms are applied to the embeddings.
Finally, the embeddings are visualized in a lower-dimensional space to
understand the feasibility of the clustering process.