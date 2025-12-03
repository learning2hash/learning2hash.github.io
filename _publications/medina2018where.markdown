---
layout: publication
title: Where Is This? Video Geolocation Based On Neural Network Features
authors: Salvador Medina, Zhuyun Dai, Yingkai Gao
conference: Arxiv
year: 2018
bibkey: medina2018where
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09068'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Neural Hashing"]
short_authors: Salvador Medina, Zhuyun Dai, Yingkai Gao
---
In this work we propose a method that geolocates videos within a delimited
widespread area based solely on the frames visual content. Our proposed method
tackles video-geolocation through traditional image retrieval techniques
considering Google Street View as the reference point. To achieve this goal we
use the deep learning features obtained from NetVLAD to represent images, since
through this feature vectors the similarity is their L2 norm. In this paper, we
propose a family of voting-based methods to aggregate frame-wise geolocation
results which boost the video geolocation result. The best aggregation found
through our experiments considers both NetVLAD and SIFT similarity, as well as
the geolocation density of the most similar results. To test our proposed
method, we gathered a new video dataset from Pittsburgh Downtown area to
benefit and stimulate more work in this area. Our system achieved a precision
of 90% while geolocating videos within a range of 150 meters or two blocks away
from the original position.