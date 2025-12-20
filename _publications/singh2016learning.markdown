---
layout: publication
title: Learning To Hash-tag Videos With Tag2vec
authors: Aditya Singh, Saurabh Saini, Rajvi Shah, Pj Narayanan
conference: Proceedings of the Tenth Indian Conference on Computer Vision, Graphics
  and Image Processing
year: 2016
bibkey: singh2016learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.04061'}]
tags: ["Evaluation", "Hashing Methods", "Recommender Systems"]
short_authors: Singh et al.
---
User-given tags or labels are valuable resources for semantic understanding
of visual media such as images and videos. Recently, a new type of labeling
mechanism known as hash-tags have become increasingly popular on social media
sites. In this paper, we study the problem of generating relevant and useful
hash-tags for short video clips. Traditional data-driven approaches for tag
enrichment and recommendation use direct visual similarity for label transfer
and propagation. We attempt to learn a direct low-cost mapping from video to
hash-tags using a two step training process. We first employ a natural language
processing (NLP) technique, skip-gram models with neural network training to
learn a low-dimensional vector representation of hash-tags (Tag2Vec) using a
corpus of 10 million hash-tags. We then train an embedding function to map
video features to the low-dimensional Tag2vec space. We learn this embedding
for 29 categories of short video clips with hash-tags. A query video without
any tag-information can then be directly mapped to the vector space of tags
using the learned embedding and relevant tags can be found by performing a
simple nearest-neighbor retrieval in the Tag2Vec space. We validate the
relevance of the tags suggested by our system qualitatively and quantitatively
with a user study.