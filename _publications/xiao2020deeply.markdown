---
layout: publication
title: Deeply Activated Salient Region For Instance Search
authors: Hui-chu Xiao, Wan-lei Zhao, Jie Lin, Chong-wah Ngo
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2022
bibkey: xiao2020deeply
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00185'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Xiao et al.
---
The performance of instance search depends heavily on the ability to locate
and describe a wide variety of object instances in a video/image collection.
Due to the lack of proper mechanism in locating instances and deriving feature
representation, instance search is generally only effective for retrieving
instances of known object categories. In this paper, a simple but effective
instance-level feature representation is presented. Different from other
approaches, the issues in class-agnostic instance localization and distinctive
feature representation are considered. The former is achieved by detecting
salient instance regions from an image by a layer-wise back-propagation
process. The back-propagation starts from the last convolution layer of a
pre-trained CNN that is originally used for classification. The
back-propagation proceeds layer-by-layer until it reaches the input layer. This
allows the salient instance regions in the input image from both known and
unknown categories to be activated. Each activated salient region covers the
full or more usually a major range of an instance. The distinctive feature
representation is produced by average-pooling on the feature map of certain
layer with the detected instance region. Experiments show that such kind of
feature representation demonstrates considerably better performance over most
of the existing approaches. In addition, we show that the proposed feature
descriptor is also suitable for content-based image search.