---
layout: publication
title: Neural Dataset Generality
authors: Ragav Venkatesan, Vijetha Gattupalli, Baoxin Li
conference: Arxiv
year: 2016
bibkey: venkatesan2016neural
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.04369'}]
tags: ["Datasets"]
short_authors: Ragav Venkatesan, Vijetha Gattupalli, Baoxin Li
---
Often the filters learned by Convolutional Neural Networks (CNNs) from
different datasets appear similar. This is prominent in the first few layers.
This similarity of filters is being exploited for the purposes of transfer
learning and some studies have been made to analyse such transferability of
features. This is also being used as an initialization technique for different
tasks in the same dataset or for the same task in similar datasets.
Off-the-shelf CNN features have capitalized on this idea to promote their
networks as best transferable and most general and are used in a cavalier
manner in day-to-day computer vision tasks.
  It is curious that while the filters learned by these CNNs are related to the
atomic structures of the images from which they are learnt, all datasets learn
similar looking low-level filters. With the understanding that a dataset that
contains many such atomic structures learn general filters and are therefore
useful to initialize other networks with, we propose a way to analyse and
quantify generality among datasets from their accuracies on transferred
filters. We applied this metric on several popular character recognition,
natural image and a medical image dataset, and arrived at some interesting
conclusions. On further experimentation we also discovered that particular
classes in a dataset themselves are more general than others.