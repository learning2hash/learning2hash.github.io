---
layout: publication
title: 'Teaching A New Dog Old Tricks: Resurrecting Multilingual Retrieval Using Zero-shot
  Learning'
authors: Sean Macavaney, Luca Soldaini, Nazli Goharian
conference: Lecture Notes in Computer Science
year: 2020
bibkey: macavaney2019teaching
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.13080'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Sean Macavaney, Luca Soldaini, Nazli Goharian
---
While billions of non-English speaking users rely on search engines every
day, the problem of ad-hoc information retrieval is rarely studied for
non-English languages. This is primarily due to a lack of data set that are
suitable to train ranking algorithms. In this paper, we tackle the lack of data
by leveraging pre-trained multilingual language models to transfer a retrieval
system trained on English collections to non-English queries and documents. Our
model is evaluated in a zero-shot setting, meaning that we use them to predict
relevance scores for query-document pairs in languages never seen during
training. Our results show that the proposed approach can significantly
outperform unsupervised retrieval techniques for Arabic, Chinese Mandarin, and
Spanish. We also show that augmenting the English training collection with some
examples from the target language can sometimes improve performance.