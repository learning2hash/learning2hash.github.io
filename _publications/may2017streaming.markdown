---
layout: publication
title: Streaming Word Embeddings With The Space-saving Algorithm
authors: Chandler May, Kevin Duh, Benjamin van Durme, Ashwin Lall
conference: Arxiv
year: 2017
bibkey: may2017streaming
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.07463'}]
tags: []
short_authors: May et al.
---
We develop a streaming (one-pass, bounded-memory) word embedding algorithm
based on the canonical skip-gram with negative sampling algorithm implemented
in word2vec. We compare our streaming algorithm to word2vec empirically by
measuring the cosine similarity between word pairs under each algorithm and by
applying each algorithm in the downstream task of hashtag prediction on a
two-month interval of the Twitter sample stream. We then discuss the results of
these experiments, concluding they provide partial validation of our approach
as a streaming replacement for word2vec. Finally, we discuss potential failure
modes and suggest directions for future work.