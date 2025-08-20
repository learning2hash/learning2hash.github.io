---
layout: publication
title: 'Doctag2vec: An Embedding Based Multi-label Learning Approach For Document
  Tagging'
authors: Sheng Chen, Akshay Soni, Aasish Pappu, Yashar Mehdad
conference: Proceedings of the 2nd Workshop on Representation Learning for NLP
year: 2017
bibkey: chen2017doctag2vec
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.04596'}]
tags: [Recommender Systems, Datasets]
short_authors: Chen et al.
---
Tagging news articles or blog posts with relevant tags from a collection of
predefined ones is coined as document tagging in this work. Accurate tagging of
articles can benefit several downstream applications such as recommendation and
search. In this work, we propose a novel yet simple approach called DocTag2Vec
to accomplish this task. We substantially extend Word2Vec and Doc2Vec---two
popular models for learning distributed representation of words and documents.
In DocTag2Vec, we simultaneously learn the representation of words, documents,
and tags in a joint vector space during training, and employ the simple
\(k\)-nearest neighbor search to predict tags for unseen documents. In contrast
to previous multi-label learning methods, DocTag2Vec directly deals with raw
text instead of provided feature vector, and in addition, enjoys advantages
like the learning of tag representation, and the ability of handling newly
created tags. To demonstrate the effectiveness of our approach, we conduct
experiments on several datasets and show promising results against
state-of-the-art methods.