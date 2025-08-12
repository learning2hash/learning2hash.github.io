---
layout: publication
title: Building Instance Classification Using Street View Images
authors: "Jian Kang, Marco K\xF6rner, Yuanyuan Wang, Hannes Taubenb\xF6ck, Xiao Xiang\
  \ Zhu"
conference: ISPRS Journal of Photogrammetry and Remote Sensing
year: 2018
bibkey: kang2018building
citations: 312
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.09026'}]
tags: []
short_authors: Kang et al.
---
Land-use classification based on spaceborne or aerial remote sensing images
has been extensively studied over the past decades. Such classification is
usually a patch-wise or pixel-wise labeling over the whole image. But for many
applications, such as urban population density mapping or urban utility
planning, a classification map based on individual buildings is much more
informative. However, such semantic classification still poses some fundamental
challenges, for example, how to retrieve fine boundaries of individual
buildings. In this paper, we proposed a general framework for classifying the
functionality of individual buildings. The proposed method is based on
Convolutional Neural Networks (CNNs) which classify facade structures from
street view images, such as Google StreetView, in addition to remote sensing
images which usually only show roof structures. Geographic information was
utilized to mask out individual buildings, and to associate the corresponding
street view images. We created a benchmark dataset which was used for training
and evaluating CNNs. In addition, the method was applied to generate building
classification maps on both region and city scales of several cities in Canada
and the US. Keywords: CNN, Building instance classification, Street view
images, OpenStreetMap