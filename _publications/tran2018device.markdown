---
layout: publication
title: On-device Scalable Image-based Localization Via Prioritized Cascade Search
  And Fast One-many RANSAC
authors: Ngoc-trung Tran, Dang-khoa Le Tan, Anh-dzung Doan, Thanh-toan Do, Tuan-anh
  Bui, Mengxuan Tan, Ngai-man Cheung
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: tran2018device
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.03510'}]
tags: ["Scalability"]
short_authors: Tran et al.
---
We present the design of an entire on-device system for large-scale urban
localization using images. The proposed design integrates compact image
retrieval and 2D-3D correspondence search to estimate the location in extensive
city regions. Our design is GPS agnostic and does not require network
connection. In order to overcome the resource constraints of mobile devices, we
propose a system design that leverages the scalability advantage of image
retrieval and accuracy of 3D model-based localization. Furthermore, we propose
a new hashing-based cascade search for fast computation of 2D-3D
correspondences. In addition, we propose a new one-many RANSAC for accurate
pose estimation. The new one-many RANSAC addresses the challenge of repetitive
building structures (e.g. windows, balconies) in urban localization. Extensive
experiments demonstrate that our 2D-3D correspondence search achieves
state-of-the-art localization accuracy on multiple benchmark datasets.
Furthermore, our experiments on a large Google Street View (GSV) image dataset
show the potential of large-scale localization entirely on a typical mobile
device.