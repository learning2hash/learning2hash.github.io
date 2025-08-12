---
layout: publication
title: 'FLAIR: Federated Learning Annotated Image Repository'
authors: Congzheng Song, Filip Granqvist, Kunal Talwar
conference: Arxiv
year: 2022
bibkey: song2022flair
citations: 3
additional_links: [{name: Code, url: 'https://github.com/apple/ml-flair'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.08869'}]
tags: ["Datasets", "Evaluation"]
short_authors: Congzheng Song, Filip Granqvist, Kunal Talwar
---
Cross-device federated learning is an emerging machine learning (ML) paradigm
where a large population of devices collectively train an ML model while the
data remains on the devices. This research field has a unique set of practical
challenges, and to systematically make advances, new datasets curated to be
compatible with this paradigm are needed. Existing federated learning
benchmarks in the image domain do not accurately capture the scale and
heterogeneity of many real-world use cases. We introduce FLAIR, a challenging
large-scale annotated image dataset for multi-label classification suitable for
federated learning. FLAIR has 429,078 images from 51,414 Flickr users and
captures many of the intricacies typically encountered in federated learning,
such as heterogeneous user data and a long-tailed label distribution. We
implement multiple baselines in different learning setups for different tasks
on this dataset. We believe FLAIR can serve as a challenging benchmark for
advancing the state-of-the art in federated learning. Dataset access and the
code for the benchmark are available at
https://github.com/apple/ml-flair.