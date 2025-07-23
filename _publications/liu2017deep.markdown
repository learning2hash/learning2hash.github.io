---
layout: publication
title: Deep Hashing With Category Mask For Fast Video Retrieval
authors: Liu Xu, Zhao Lili, Ding Dajun, Dong Yajiao
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: liu2017deep
citations: 267
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.08315'}]
tags: ["CVPR", "Hashing Methods", "Neural Hashing", "Supervised", "Video Retrieval"]
short_authors: Liu et al.
---
This paper proposes an end-to-end deep hashing framework with category mask
for fast video retrieval. We train our network in a supervised way by fully
exploiting inter-class diversity and intra-class identity. Classification loss
is optimized to maximize inter-class diversity, while intra-pair is introduced
to learn representative intra-class identity. We investigate the binary bits
distribution related to categories and find out that the effectiveness of
binary bits is highly correlated with data categories, and some bits may
degrade classification performance of some categories. We then design hash code
generation scheme with category mask to filter out bits with negative
contribution. Experimental results demonstrate the proposed method outperforms
several state-of-the-arts under various evaluation metrics on public datasets.