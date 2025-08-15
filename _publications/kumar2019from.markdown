---
layout: publication
title: From Fully Supervised To Zero Shot Settings For Twitter Hashtag Recommendation
authors: Abhay Kumar, Nishant Jain, Suraj Tripathi, Chirag Singh
conference: Arxiv
year: 2019
bibkey: kumar2019from
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.04914'}]
tags: ["Evaluation", "Recommender Systems", "Scalability", "Supervised"]
short_authors: Kumar et al.
---
We propose a comprehensive end-to-end pipeline for Twitter hashtags
recommendation system including data collection, supervised training setting
and zero shot training setting. In the supervised training setting, we have
proposed and compared the performance of various deep learning architectures,
namely Convolutional Neural Network (CNN), Recurrent Neural Network (RNN) and
Transformer Network. However, it is not feasible to collect data for all
possible hashtag labels and train a classifier model on them. To overcome this
limitation, we propose a Zero Shot Learning (ZSL) paradigm for predicting
unseen hashtag labels by learning the relationship between the semantic space
of tweets and the embedding space of hashtag labels. We evaluated various
state-of-the-art ZSL methods like Convex combination of Semantic Embedding
(ConSE), Embarrassingly Simple Zero-Shot Learning (ESZSL) and Deep Embedding
Model for Zero-Shot Learning (DEM-ZSL) for the hashtag recommendation task. We
demonstrate the effectiveness and scalability of ZSL methods for the
recommendation of unseen hashtags. To the best of our knowledge, this is the
first quantitative evaluation of ZSL methods to date for unseen hashtags
recommendations from tweet text.