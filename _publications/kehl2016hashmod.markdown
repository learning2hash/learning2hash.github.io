---
layout: publication
title: "Hashmod: A Hashing Method for Scalable 3D Object Detection"
authors: Kehl Wadim, Tombari Federico, Navab Nassir, Ilic Slobodan, Lepetit Vincent
conference: Arxiv
year: 2016
bibkey: kehl2016hashmod
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1607.06062"}
tags: ['ARXIV']
---
We present a scalable method for detecting objects and estimating their 3D poses in RGB-D data. To this end, we rely on an efficient representation of object views and employ hashing techniques to match these views against the input frame in a scalable way. While a similar approach already exists for 2D detection, we show how to extend it to estimate the 3D pose of the detected objects. In particular, we explore different hashing strategies and identify the one which is more suitable to our problem. We show empirically that the complexity of our method is sublinear with the number of objects and we enable detection and pose estimation of many 3D objects with high accuracy while outperforming the state-of-the-art in terms of runtime.