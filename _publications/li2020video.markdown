---
layout: publication
title: 'Video Face Recognition System: Retinaface-mnet-faster And Secondary Search'
authors: Qian Li, Nan Guo, Xiaochun Ye, Dongrui Fan, Zhimin Tang
conference: Arxiv
year: 2020
bibkey: li2020video
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.13167'}]
tags: ["Datasets", "Evaluation", "Graph Based ANN", "Scalability"]
short_authors: Li et al.
---
Face recognition is widely used in the scene. However, different visual
environments require different methods, and face recognition has a difficulty
in complex environments. Therefore, this paper mainly experiments complex faces
in the video. First, we design an image pre-processing module for fuzzy scene
or under-exposed faces to enhance images. Our experimental results demonstrate
that effective images pre-processing improves the accuracy of 0.11%, 0.2% and
1.4% on LFW, WIDER FACE and our datasets, respectively. Second, we propose
RetinacFace-mnet-faster for detection and a confidence threshold specification
for face recognition, reducing the lost rate. Our experimental results show
that our RetinaFace-mnet-faster for 640*480 resolution on the Tesla P40 and
single-thread improve speed of 16.7% and 70.2%, respectively. Finally, we
design secondary search mechanism with HNSW to improve performance. Ours is
suitable for large-scale datasets, and experimental results show that our
method is 82% faster than the violent retrieval for the single-frame detection.