---
layout: publication
title: Given Users Recommendations Based On Reviews On Yelp
authors: Zhang Shuwei, Tang Maiqi, Zhang Qingyang, Luo Yucan, Zou Yuhui
conference: Arxiv
year: 2021
bibkey: zhang2021given
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01762'}]
tags: ["Survey-Paper", "Recommender-Systems"]
short_authors: Zhang et al.
---
In our project, we focus on NLP-based hybrid recommendation systems. Our data
is from Yelp Data. For our hybrid recommendation system, we have two major
components: the first part is to embed the reviews with the Bert model and
word2vec model; the second part is the implementation of an item-based
collaborative filtering algorithm to compute the similarity of each review
under different categories of restaurants. In the end, with the help of
similarity scores, we are able to recommend users the most matched restaurant
based on their recorded reviews. The coding work is split into several parts:
selecting samples and data cleaning, processing, embedding, computing
similarity, and computing prediction and error. Due to the size of the data,
each part will generate one or more JSON files as the milestone to reduce the
pressure on memory and the communication between each part.