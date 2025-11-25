---
layout: publication
title: Neural Aggregation Network For Video Face Recognition
authors: Jiaolong Yang, Peiran Ren, Dongqing Zhang, Dong Chen, Fang Wen, Hongdong
  Li, Gang Hua
conference: Arxiv
year: 2016
bibkey: yang2016neural
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.05474'}]
tags: ["Evaluation", "Image Retrieval", "Supervised", "Video Retrieval"]
short_authors: Yang et al.
---
This paper presents a Neural Aggregation Network (NAN) for video face
recognition. The network takes a face video or face image set of a person with
a variable number of face images as its input, and produces a compact,
fixed-dimension feature representation for recognition. The whole network is
composed of two modules. The feature embedding module is a deep Convolutional
Neural Network (CNN) which maps each face image to a feature vector. The
aggregation module consists of two attention blocks which adaptively aggregate
the feature vectors to form a single feature inside the convex hull spanned by
them. Due to the attention mechanism, the aggregation is invariant to the image
order. Our NAN is trained with a standard classification or verification loss
without any extra supervision signal, and we found that it automatically learns
to advocate high-quality face images while repelling low-quality ones such as
blurred, occluded and improperly exposed faces. The experiments on IJB-A,
YouTube Face, Celebrity-1000 video face recognition benchmarks show that it
consistently outperforms naive aggregation methods and achieves the
state-of-the-art accuracy.