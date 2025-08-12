---
layout: publication
title: 'Bounding Boxes Are All We Need: Street View Image Classification Via Context
  Encoding Of Detected Buildings'
authors: Kun Zhao, Yongkun Liu, Siyuan Hao, Shaoxing Lu, Hongbin Liu, Lijian Zhou
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2021
bibkey: zhao2020bounding
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.01305'}]
tags: []
short_authors: Zhao et al.
---
Street view images classification aiming at urban land use analysis is
difficult because the class labels (e.g., commercial area), are concepts with
higher abstract level compared to the ones of general visual tasks (e.g.,
persons and cars). Therefore, classification models using only visual features
often fail to achieve satisfactory performance. In this paper, a novel approach
based on a "Detector-Encoder-Classifier" framework is proposed. Instead of
using visual features of the whole image directly as common image-level models
based on convolutional neural networks (CNNs) do, the proposed framework
firstly obtains the bounding boxes of buildings in street view images from a
detector. Their contextual information such as the co-occurrence patterns of
building classes and their layout are then encoded into metadata by the
proposed algorithm "CODING" (Context encOding of Detected buildINGs). Finally,
these bounding box metadata are classified by a recurrent neural network (RNN).
In addition, we made a dual-labeled dataset named "BEAUTY" (Building dEtection
And Urban funcTional-zone portraYing) of 19,070 street view images and 38,857
buildings based on the existing BIC GSV [1]. The dataset can be used not only
for street view image classification, but also for multi-class building
detection. Experiments on "BEAUTY" show that the proposed approach achieves a
12.65% performance improvement on macro-precision and 12% on macro-recall over
image-level CNN based models. Our code and dataset are available at
https://github.com/kyle-one/Context-Encoding-of-Detected-Buildings/