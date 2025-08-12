---
layout: publication
title: Are Word Embedding-based Features Useful For Sarcasm Detection?
authors: Aditya Joshi, Vaibhav Tripathi, Kevin Patel, Pushpak Bhattacharyya, Mark
  Carman
conference: Proceedings of the 2016 Conference on Empirical Methods in Natural Language
  Processing
year: 2016
bibkey: joshi2016are
citations: 172
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.00883'}]
tags: ["EMNLP"]
short_authors: Joshi et al.
---
This paper makes a simple increment to state-of-the-art in sarcasm detection
research. Existing approaches are unable to capture subtle forms of context
incongruity which lies at the heart of sarcasm. We explore if prior work can be
enhanced using semantic similarity/discordance between word embeddings. We
augment word embedding-based features to four feature sets reported in the
past. We also experiment with four types of word embeddings. We observe an
improvement in sarcasm detection, irrespective of the word embedding used or
the original feature set to which our features are augmented. For example, this
augmentation results in an improvement in F-score of around 4% for three out
of these four feature sets, and a minor degradation in case of the fourth, when
Word2Vec embeddings are used. Finally, a comparison of the four embeddings
shows that Word2Vec and dependency weight-based features outperform LSA and
GloVe, in terms of their benefit to sarcasm detection.