---
layout: publication
title: Towards Predicting The Likeability Of Fashion Images
authors: Jinghua Wang, Abrar Abdul Nabi, Gang Wang, Chengde Wan, Tian-Tsong Ng
conference: Arxiv
year: 2015
bibkey: wang2015towards
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.05296'}]
tags: ["Datasets"]
short_authors: Wang et al.
---
In this paper, we propose a method for ranking fashion images to find the
ones which might be liked by more people. We collect two new datasets from
image sharing websites (Pinterest and Polyvore). We represent fashion images
based on attributes: semantic attributes and data-driven attributes. To learn
semantic attributes from limited training data, we use an algorithm on
multi-task convolutional neural networks to share visual knowledge among
different semantic attribute categories. To discover data-driven attributes
unsupervisedly, we propose an algorithm to simultaneously discover visual
clusters and learn fashion-specific feature representations. Given attributes
as representations, we propose to learn a ranking SPN (sum product networks) to
rank pairs of fashion images. The proposed ranking SPN can capture the
high-order correlations of the attributes. We show the effectiveness of our
method on our two newly collected datasets.