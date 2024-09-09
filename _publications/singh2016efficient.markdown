---
layout: publication
title: Efficient Document Indexing Using Pivot Tree
authors: Singh Gaurav, Piwowarski Benjamin
conference: "Arxiv"
year: 2016
bibkey: singh2016efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.06693"}
tags: ['ARXIV']
---
We present a novel method for efficiently searching top-k neighbors for documents represented in high dimensional space of terms based on the cosine similarity. Mostly documents are stored as bag-of-words tf-idf representation. One of the most used ways of computing similarity between a pair of documents is cosine similarity between the vector representations but cosine similarity is not a metric distance measure as it doesnt follow triangle inequality therefore most metric searching methods can not be applied directly. We propose an efficient method for indexing documents using a pivot tree that leads to efficient retrieval. We also study the relation between precision and efficiency for the proposed method and compare it with a state of the art in the area of document searching based on inner product.
