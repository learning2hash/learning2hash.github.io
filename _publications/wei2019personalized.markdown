---
layout: publication
title: Personalized Hashtag Recommendation For Micro-videos
authors: Yinwei Wei, Zhiyong Cheng, Xuzheng Yu, Zhou Zhao, Lei Zhu, Liqiang Nie
conference: Proceedings of the 27th ACM International Conference on Multimedia
year: 2019
bibkey: wei2019personalized
citations: 80
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.09987'}]
tags: ["Recommender Systems"]
short_authors: Wei et al.
---
Personalized hashtag recommendation methods aim to suggest users hashtags to
annotate, categorize, and describe their posts. The hashtags, that a user
provides to a post (e.g., a micro-video), are the ones which in her mind can
well describe the post content where she is interested in. It means that we
should consider both users' preferences on the post contents and their personal
understanding on the hashtags. Most existing methods rely on modeling either
the interactions between hashtags and posts or the interactions between users
and hashtags for hashtag recommendation. These methods have not well explored
the complicated interactions among users, hashtags, and micro-videos. In this
paper, towards the personalized micro-video hashtag recommendation, we propose
a Graph Convolution Network based Personalized Hashtag Recommendation (GCN-PHR)
model, which leverages recently advanced GCN techniques to model the complicate
interactions among <users, hashtags, micro-videos> and learn their
representations. In our model, the users, hashtags, and micro-videos are three
types of nodes in a graph and they are linked based on their direct
associations. In particular, the message-passing strategy is used to learn the
representation of a node (e.g., user) by aggregating the message passed from
the directly linked other types of nodes (e.g., hashtag and micro-video).
Because a user is often only interested in certain parts of a micro-video and a
hashtag is typically used to describe the part (of a micro-video) that the user
is interested in, we leverage the attention mechanism to filter the message
passed from micro-videos to users and hashtags, which can significantly improve
the representation capability. Extensive experiments have been conducted on two
real-world micro-video datasets and demonstrate that our model outperforms the
state-of-the-art approaches by a large margin.