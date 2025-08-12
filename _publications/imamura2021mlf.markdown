---
layout: publication
title: 'MLF-SC: Incorporating Multi-layer Features To Sparse Coding For Anomaly Detection'
authors: Ryuji Imamura, Kohei Azuma, Atsushi Hanamoto, Atsunori Kanemura
conference: Arxiv
year: 2021
bibkey: imamura2021mlf
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.04289'}]
tags: []
short_authors: Imamura et al.
---
Anomalies in images occur in various scales from a small hole on a carpet to
a large stain. However, anomaly detection based on sparse coding, one of the
widely used anomaly detection methods, has an issue in dealing with anomalies
that are out of the patch size employed to sparsely represent images. A large
anomaly can be considered normal if seen in a small scale, but it is not easy
to determine a single scale (patch size) that works well for all images. Then,
we propose to incorporate multi-scale features to sparse coding and improve the
performance of anomaly detection. The proposed method, multi-layer feature
sparse coding (MLF-SC), employs a neural network for feature extraction, and
feature maps from intermediate layers of the network are given to sparse
coding, whereas the standard sparse-coding-based anomaly detection method
directly works on given images. We show that MLF-SC outperforms
state-of-the-art anomaly detection methods including those employing deep
learning. Our target data are the texture categories of the MVTec Anomaly
Detection (MVTec AD) dataset, which is a modern benchmark dataset consisting of
images from the real world. Our idea can be a simple and practical option to
deal with practical data.