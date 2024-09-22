---
layout: publication
title: Compact Deep Aggregation for Set Retrieval
authors: Zhong Yujie, Arandjelović Relja, Zisserman Andrew
conference: "Arxiv"
year: 2020
bibkey: zhong2020compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2003.11794"}
tags: ['ARXIV', 'CNN', 'General', 'TIP', 'Text Retrieval']
---
The objective of this work is to learn a compact embedding of a set of descriptors that is suitable for efficient retrieval and ranking whilst maintaining discriminability of the individual descriptors. We focus on a specific example of this general problem -- that of retrieving images containing multiple faces from a large scale dataset of images. Here the set consists of the face descriptors in each image and given a query for multiple identities the goal is then to retrieve in order images which contain all the identities all but one etc To this end we make the following contributions first we propose a CNN architecture -- em SetNet -- to achieve the objective it learns face descriptors and their aggregation over a set to produce a compact fixed length descriptor designed for set retrieval and the score of an image is a count of the number of identities that match the query; second we show that this compact descriptor has minimal loss of discriminability up to two faces per image and degrades slowly after that -- far exceeding a number of baselines; third we explore the speed vs. retrieval quality trade-off for set retrieval using this compact descriptor; and finally we collect and annotate a large dataset of images containing various number of celebrities which we use for evaluation and is publicly released.
