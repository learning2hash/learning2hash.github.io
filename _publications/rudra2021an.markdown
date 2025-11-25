---
layout: publication
title: An In-depth Analysis Of Passage-level Label Transfer For Contextual Document
  Ranking
authors: Koustav Rudra, Zeon Trevor Fernando, Avishek Anand
conference: Arxiv
year: 2021
bibkey: rudra2021an
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16669'}]
tags: ["Datasets", "Efficiency", "Text Retrieval"]
short_authors: Koustav Rudra, Zeon Trevor Fernando, Avishek Anand
---
Pre-trained contextual language models such as BERT, GPT, and XLnet work
quite well for document retrieval tasks. Such models are fine-tuned based on
the query-document/query-passage level relevance labels to capture the ranking
signals. However, the documents are longer than the passages and such document
ranking models suffer from the token limitation (512) of BERT. Researchers
proposed ranking strategies that either truncate the documents beyond the token
limit or chunk the documents into units that can fit into the BERT. In the
later case, the relevance labels are either directly transferred from the
original query-document pair or learned through some external model. In this
paper, we conduct a detailed study of the design decisions about splitting and
label transfer on retrieval effectiveness and efficiency. We find that direct
transfer of relevance labels from documents to passages introduces label noise
that strongly affects retrieval effectiveness for large training datasets. We
also find that query processing times are adversely affected by fine-grained
splitting schemes. As a remedy, we propose a careful passage level labelling
scheme using weak supervision that delivers improved performance (3-14% in
terms of nDCG score) over most of the recently proposed models for ad-hoc
retrieval while maintaining manageable computational complexity on four diverse
document retrieval datasets.