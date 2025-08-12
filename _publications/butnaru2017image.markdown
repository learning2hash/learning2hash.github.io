---
layout: publication
title: 'From Image To Text Classification: A Novel Approach Based On Clustering Word
  Embeddings'
authors: Andrei M. Butnaru, Radu Tudor Ionescu
conference: Procedia Computer Science
year: 2017
bibkey: butnaru2017image
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.08098'}]
tags: ["Evaluation"]
short_authors: Andrei M. Butnaru, Radu Tudor Ionescu
---
In this paper, we propose a novel approach for text classification based on
clustering word embeddings, inspired by the bag of visual words model, which is
widely used in computer vision. After each word in a collection of documents is
represented as word vector using a pre-trained word embeddings model, a k-means
algorithm is applied on the word vectors in order to obtain a fixed-size set of
clusters. The centroid of each cluster is interpreted as a super word embedding
that embodies all the semantically related word vectors in a certain region of
the embedding space. Every embedded word in the collection of documents is then
assigned to the nearest cluster centroid. In the end, each document is
represented as a bag of super word embeddings by computing the frequency of
each super word embedding in the respective document. We also diverge from the
idea of building a single vocabulary for the entire collection of documents,
and propose to build class-specific vocabularies for better performance. Using
this kind of representation, we report results on two text mining tasks, namely
text categorization by topic and polarity classification. On both tasks, our
model yields better performance than the standard bag of words.