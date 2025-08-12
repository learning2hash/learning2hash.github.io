---
layout: publication
title: 'Link Prediction By De-anonymization: How We Won The Kaggle Social Network
  Challenge'
authors: Arvind Narayanan, Elaine Shi, Benjamin I. P. Rubinstein
conference: The 2011 International Joint Conference on Neural Networks
year: 2011
bibkey: narayanan2011link
citations: 164
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1102.4374'}]
tags: []
short_authors: Arvind Narayanan, Elaine Shi, Benjamin I. P. Rubinstein
---
This paper describes the winning entry to the IJCNN 2011 Social Network
Challenge run by Kaggle.com. The goal of the contest was to promote research on
real-world link prediction, and the dataset was a graph obtained by crawling
the popular Flickr social photo sharing website, with user identities scrubbed.
By de-anonymizing much of the competition test set using our own Flickr crawl,
we were able to effectively game the competition. Our attack represents a new
application of de-anonymization to gaming machine learning contests, suggesting
changes in how future competitions should be run.
  We introduce a new simulated annealing-based weighted graph matching
algorithm for the seeding step of de-anonymization. We also show how to combine
de-anonymization with link prediction---the latter is required to achieve good
performance on the portion of the test set not de-anonymized---for example by
training the predictor on the de-anonymized portion of the test set, and
combining probabilistic predictions from de-anonymization and link prediction.