---
layout: publication
title: Accelerating Spatio-textual Queries With Learned Indices
authors: Georgios Chatzigeorgakidis, Kostas Patroumpas, Dimitrios Skoutas, Spiros
  Athanasiou
conference: Arxiv
year: 2023
bibkey: chatzigeorgakidis2023accelerating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09864'}]
tags: ["Datasets", "Evaluation", "Hybrid ANN Methods", "Vector Indexing"]
short_authors: Chatzigeorgakidis et al.
---
Efficiently computing spatio-textual queries has become increasingly
important in various applications that need to quickly retrieve geolocated
entities associated with textual information, such as in location-based
services and social networks. To accelerate such queries, several works have
proposed combining spatial and textual indices into hybrid index structures.
Recently, the novel idea of replacing traditional indices with ML models has
attracted a lot of attention. This includes works on learned spatial indices,
where the main challenge is to address the lack of a total ordering among
objects in a multidimensional space. In this work, we investigate how to extend
this novel type of index design to the case of spatio-textual data. We study
different design choices, based on either loose or tight coupling between the
spatial and textual part, as well as a hybrid index that combines a traditional
and a learned component. We also perform an experimental evaluation using
several real-world datasets to assess the potential benefits of using a learned
index for evaluating spatio-textual queries.