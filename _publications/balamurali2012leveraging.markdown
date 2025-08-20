---
layout: publication
title: Leveraging Sentiment To Compute Word Similarity
authors: A. R. Balamurali, Subhabrata Mukherjee, Akshat Malu, Pushpak Bhattacharyya
conference: In Proceedings of The 6th International Global Wordnet Conference (GWC
  2012) Matsue Japan January 9-13 2012
year: 2012
bibkey: balamurali2012leveraging
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1209.2341'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Balamurali et al.
---
In this paper, we introduce a new WordNet based similarity metric, SenSim,
which incorporates sentiment content (i.e., degree of positive or negative
sentiment) of the words being compared to measure the similarity between them.
The proposed metric is based on the hypothesis that knowing the sentiment is
beneficial in measuring the similarity. To verify this hypothesis, we measure
and compare the annotator agreement for 2 annotation strategies: 1) sentiment
information of a pair of words is considered while annotating and 2) sentiment
information of a pair of words is not considered while annotating.
Inter-annotator correlation scores show that the agreement is better when the
two annotators consider sentiment information while assigning a similarity
score to a pair of words. We use this hypothesis to measure the similarity
between a pair of words. Specifically, we represent each word as a vector
containing sentiment scores of all the content words in the WordNet gloss of
the sense of that word. These sentiment scores are derived from a sentiment
lexicon. We then measure the cosine similarity between the two vectors. We
perform both intrinsic and extrinsic evaluation of SenSim and compare the
performance with other widely usedWordNet similarity metrics.