---
layout: publication
title: 'Emtagger: A Word Embedding Based Novel Method For Hashtag Recommendation On
  Twitter'
authors: Kuntal Dey, Ritvik Shrivastava, Saroj Kaushik, L. Venkata Subramaniam
conference: 2017 IEEE International Conference on Data Mining Workshops (ICDMW)
year: 2017
bibkey: dey2017emtagger
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.01562'}]
tags: [Recommender Systems, Tools & Libraries]
short_authors: Dey et al.
---
The hashtag recommendation problem addresses recommending (suggesting) one or
more hashtags to explicitly tag a post made on a given social network platform,
based upon the content and context of the post. In this work, we propose a
novel methodology for hashtag recommendation for microblog posts, specifically
Twitter. The methodology, EmTaggeR, is built upon a training-testing framework
that builds on the top of the concept of word embedding. The training phase
comprises of learning word vectors associated with each hashtag, and deriving a
word embedding for each hashtag. We provide two training procedures, one in
which each hashtag is trained with a separate word embedding model applicable
in the context of that hashtag, and another in which each hashtag obtains its
embedding from a global context. The testing phase constitutes computing the
average word embedding of the test post, and finding the similarity of this
embedding with the known embeddings of the hashtags. The tweets that contain
the most-similar hashtag are extracted, and all the hashtags that appear in
these tweets are ranked in terms of embedding similarity scores. The top-K
hashtags that appear in this ranked list, are recommended for the given test
post. Our system produces F1 score of 50.83%, improving over the LDA baseline
by around 6.53 times, outperforming the best-performing system known in the
literature that provides a lift of 6.42 times. EmTaggeR is a fast, scalable and
lightweight system, which makes it practical to deploy in real-life
applications.