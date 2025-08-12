---
layout: publication
title: 'Fastenet: A Fast Railway Fastener Detector'
authors: Jun Jet Tai, Mauro S. Innocente, Owais Mehmood
conference: Lecture Notes in Networks and Systems
year: 2021
bibkey: tai2020fastenet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.07968'}]
tags: ["Evaluation"]
short_authors: Jun Jet Tai, Mauro S. Innocente, Owais Mehmood
---
In this work, a novel high-speed railway fastener detector is introduced.
This fully convolutional network, dubbed FasteNet, foregoes the notion of
bounding boxes and performs detection directly on a predicted saliency map.
Fastenet uses transposed convolutions and skip connections, the effective
receptive field of the network is 1.5\\(\times\\) larger than the average size of a
fastener, enabling the network to make predictions with high confidence,
without sacrificing output resolution. In addition, due to the saliency map
approach, the network is able to vote for the presence of a fastener up to 30
times per fastener, boosting prediction accuracy. Fastenet is capable of
running at 110 FPS on an Nvidia GTX 1080, while taking in inputs of
1600\\(\times\\)512 with an average of 14 fasteners per image. Our source is open
here: https://github.com/jjshoots/DL\_FasteNet.git