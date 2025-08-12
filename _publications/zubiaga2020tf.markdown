---
layout: publication
title: 'TF-CR: Weighting Embeddings For Text Classification'
authors: Arkaitz Zubiaga
conference: Arxiv
year: 2020
bibkey: zubiaga2020tf
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.06606'}]
tags: []
short_authors: Arkaitz Zubiaga
---
Text classification, as the task consisting in assigning categories to
textual instances, is a very common task in information science. Methods
learning distributed representations of words, such as word embeddings, have
become popular in recent years as the features to use for text classification
tasks. Despite the increasing use of word embeddings for text classification,
these are generally used in an unsupervised manner, i.e. information derived
from class labels in the training data are not exploited. While word embeddings
inherently capture the distributional characteristics of words, and contexts
observed around them in a large dataset, they aren't optimised to consider the
distributions of words across categories in the classification dataset at hand.
To optimise text representations based on word embeddings by incorporating
class distributions in the training data, we propose the use of weighting
schemes that assign a weight to embeddings of each word based on its saliency
in each class. To achieve this, we introduce a novel weighting scheme, Term
Frequency-Category Ratio (TF-CR), which can weight high-frequency,
category-exclusive words higher when computing word embeddings. Our experiments
on 16 classification datasets show the effectiveness of TF-CR, leading to
improved performance scores over existing weighting schemes, with a performance
gap that increases as the size of the training data grows.