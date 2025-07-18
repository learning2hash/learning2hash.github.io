---
layout: publication
title: End-to-end Network For Twitter Geolocation Prediction And Hashing
authors: Lau et al.
conference: Arxiv
year: 2017
bibkey: lau2017end
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.04802'}]
tags: [Compact Codes, Hashing Methods, Evaluation]
---
We propose an end-to-end neural network to predict the geolocation of a
tweet. The network takes as input a number of raw Twitter metadata such as the
tweet message and associated user account information. Our model is language
independent, and despite minimal feature engineering, it is interpretable and
capable of learning location indicative words and timing patterns. Compared to
state-of-the-art systems, our model outperforms them by 2%-6%. Additionally, we
propose extensions to the model to compress representation learnt by the
network into binary codes. Experiments show that it produces compact codes
compared to benchmark hashing algorithms. An implementation of the model is
released publicly.