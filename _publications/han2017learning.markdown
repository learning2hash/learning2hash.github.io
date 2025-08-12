---
layout: publication
title: Learning Fashion Compatibility With Bidirectional Lstms
authors: Xintong Han, Zuxuan Wu, Yu-Gang Jiang, Larry S. Davis
conference: Proceedings of the 25th ACM international conference on Multimedia
year: 2017
bibkey: han2017learning
citations: 385
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05691'}]
tags: ["Recommender Systems"]
short_authors: Han et al.
---
The ubiquity of online fashion shopping demands effective recommendation
services for customers. In this paper, we study two types of fashion
recommendation: (i) suggesting an item that matches existing components in a
set to form a stylish outfit (a collection of fashion items), and (ii)
generating an outfit with multimodal (images/text) specifications from a user.
To this end, we propose to jointly learn a visual-semantic embedding and the
compatibility relationships among fashion items in an end-to-end fashion. More
specifically, we consider a fashion outfit to be a sequence (usually from top
to bottom and then accessories) and each item in the outfit as a time step.
Given the fashion items in an outfit, we train a bidirectional LSTM (Bi-LSTM)
model to sequentially predict the next item conditioned on previous ones to
learn their compatibility relationships. Further, we learn a visual-semantic
space by regressing image features to their semantic representations aiming to
inject attribute and category information as a regularization for training the
LSTM. The trained network can not only perform the aforementioned
recommendations effectively but also predict the compatibility of a given
outfit. We conduct extensive experiments on our newly collected Polyvore
dataset, and the results provide strong qualitative and quantitative evidence
that our framework outperforms alternative methods.