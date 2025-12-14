---
layout: publication
title: 'Lightning IR: Straightforward Fine-tuning And Inference Of Transformer-based
  Language Models For Information Retrieval'
authors: "Ferdinand Schlatt, Maik Fr\xF6be, Matthias Hagen"
conference: 'WSDM ''25: The Eighteenth ACM International Conference on Web Search
  and Data Mining'
year: 2024
bibkey: schlatt2024lightning
citations: 4
additional_links: [{name: Code, url: 'https://github.com/webis-de/lightning-ir'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.04677'}]
tags: [Tools & Libraries, Re-ranking, Hybrid ANN Methods]
short_authors: "Ferdinand Schlatt, Maik Fr\xF6be, Matthias Hagen"
---
A wide range of transformer-based language models have been proposed for
information retrieval tasks. However, including transformer-based models in
retrieval pipelines is often complex and requires substantial engineering
effort. In this paper, we introduce Lightning IR, an easy-to-use PyTorch
Lightning-based framework for applying transformer-based language models in
retrieval scenarios. Lightning IR provides a modular and extensible
architecture that supports all stages of a retrieval pipeline: from fine-tuning
and indexing to searching and re-ranking. Designed to be scalable and
reproducible, Lightning IR is available as open-source:
https://github.com/webis-de/lightning-ir.