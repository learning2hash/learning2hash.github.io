---
layout: publication
title: Learning A Complete Image Indexing Pipeline
authors: "Himalaya Jain, Joaquin Zepeda, Patrick P\xE9rez, R\xE9mi Gribonval"
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: jain2017learning
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.04480'}]
tags: ["CVPR", "Hashing Methods", "Supervised", "Tools & Libraries", "Unsupervised", "Vector Indexing"]
short_authors: Jain et al.
---
To work at scale, a complete image indexing system comprises two components:
An inverted file index to restrict the actual search to only a subset that
should contain most of the items relevant to the query; An approximate distance
computation mechanism to rapidly scan these lists. While supervised deep
learning has recently enabled improvements to the latter, the former continues
to be based on unsupervised clustering in the literature. In this work, we
propose a first system that learns both components within a unifying neural
framework of structured binary encoding.