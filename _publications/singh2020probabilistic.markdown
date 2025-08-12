---
layout: publication
title: Probabilistic Random Indexing For Continuous Event Detection
authors: Yashank Singh, Niladri Chatterjee
conference: Arxiv
year: 2020
bibkey: singh2020probabilistic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.12552'}]
tags: ["Hashing Methods", "Vector Indexing"]
short_authors: Yashank Singh, Niladri Chatterjee
---
The present paper explores a novel variant of Random Indexing (RI) based
representations for encoding language data with a view to using them in a
dynamic scenario where events are happening in a continuous fashion. As the
size of the representations in the general method of onehot encoding grows
linearly with the size of the vocabulary, they become non-scalable for online
purposes with high volumes of dynamic data. On the other hand, existing
pre-trained embedding models are not suitable for detecting happenings of new
events due to the dynamic nature of the text data. The present work addresses
this issue by using a novel RI representation by imposing a probability
distribution on the number of randomized entries which leads to a class of RI
representations. It also provides a rigorous analysis of the goodness of the
representation methods to encode semantic information in terms of the
probability of orthogonality. Building on these ideas we propose an algorithm
that is log-linear with the size of vocabulary to track the semantic
relationship of a query word to other words for suggesting the events that are
relevant to the word in question. We ran simulations using the proposed
algorithm for tweet data specific to three different events and present our
findings. The proposed probabilistic RI representations are found to be much
faster and scalable than Bag of Words (BoW) embeddings while maintaining
accuracy in depicting semantic relationships.