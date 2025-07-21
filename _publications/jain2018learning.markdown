---
layout: publication
title: Learning a Complete Image Indexing Pipeline
authors: Jain et al.
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: jain2018learning
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.04480'}]
tags: ["CVPR"]
---
To work at scale, a complete image indexing system comprises two components:
An inverted file index to restrict the actual search to only a subset that
should contain most of the items relevant to the query; An approximate distance
computation mechanism to rapidly scan these lists. While supervised deep
learning has recently enabled improvements to the latter, the former continues
to be based on unsupervised clustering in the literature. In this work, we
propose a first system that learns both components within a unifying neural
framework of structured binary encoding.