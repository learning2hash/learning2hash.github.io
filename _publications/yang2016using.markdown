---
layout: publication
title: Using Word Embeddings In Twitter Election Classification
authors: Xiao Yang, Craig Macdonald, Iadh Ounis
conference: Information Retrieval Journal
year: 2017
bibkey: yang2016using
citations: 137
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07006'}]
tags: ["Datasets", "Evaluation"]
short_authors: Xiao Yang, Craig Macdonald, Iadh Ounis
---
Word embeddings and convolutional neural networks (CNN) have attracted
extensive attention in various classification tasks for Twitter, e.g. sentiment
classification. However, the effect of the configuration used to train and
generate the word embeddings on the classification performance has not been
studied in the existing literature. In this paper, using a Twitter election
classification task that aims to detect election-related tweets, we investigate
the impact of the background dataset used to train the embedding models, the
context window size and the dimensionality of word embeddings on the
classification performance. By comparing the classification results of two word
embedding models, which are trained using different background corpora (e.g.
Wikipedia articles and Twitter microposts), we show that the background data
type should align with the Twitter classification dataset to achieve a better
performance. Moreover, by evaluating the results of word embeddings models
trained using various context window sizes and dimensionalities, we found that
large context window and dimension sizes are preferable to improve the
performance. Our experimental results also show that using word embeddings and
CNN leads to statistically significant improvements over various baselines such
as random, SVM with TF-IDF and SVM with word embeddings.