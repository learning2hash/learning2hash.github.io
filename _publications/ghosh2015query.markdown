---
layout: publication
title: "Query by String word spotting based on character bi-gram indexing"
authors: Ghosh Suman K., Valveny Ernest
conference: "Arxiv"
year: 2015
bibkey: ghosh2015query
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1505.07778"}
tags: ['ARXIV']
---
In this paper we propose a segmentation-free query by string word spotting
method. Both the documents and query strings are encoded using a recently
proposed word representa- tion that projects images and strings into a common
atribute space based on a pyramidal histogram of characters(PHOC). These
attribute models are learned using linear SVMs over the Fisher Vector
representation of the images along with the PHOC labels of the corresponding
strings. In order to search through the whole page, document regions are indexed
per character bi- gram using a similar attribute representation. On top of that,
we propose an integral image representation of the document using a simplified
version of the attribute model for efficient computation. Finally we introduce a
re-ranking step in order to boost retrieval performance. We show state-of-the-
art results for segmentation-free query by string word spotting in single-writer
and multi-writer standard datasets
