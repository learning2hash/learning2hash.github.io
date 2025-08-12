---
layout: publication
title: Fine-grained Land Use Classification At The City Scale Using Ground-level Images
authors: Yi Zhu, Xueqing Deng, Shawn Newsam
conference: IEEE Transactions on Multimedia
year: 2019
bibkey: zhu2018fine
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.02668'}]
tags: ["Datasets"]
short_authors: Yi Zhu, Xueqing Deng, Shawn Newsam
---
We perform fine-grained land use mapping at the city scale using ground-level
images. Mapping land use is considerably more difficult than mapping land cover
and is generally not possible using overhead imagery as it requires close-up
views and seeing inside buildings. We postulate that the growing collections of
georeferenced, ground-level images suggest an alternate approach to this
geographic knowledge discovery problem. We develop a general framework that
uses Flickr images to map 45 different land-use classes for the City of San
Francisco. Individual images are classified using a novel convolutional neural
network containing two streams, one for recognizing objects and another for
recognizing scenes. This network is trained in an end-to-end manner directly on
the labeled training images. We propose several strategies to overcome the
noisiness of our user-generated data including search-based training set
augmentation and online adaptive training. We derive a ground truth map of San
Francisco in order to evaluate our method. We demonstrate the effectiveness of
our approach through geo-visualization and quantitative analysis. Our framework
achieves over 29% recall at the individual land parcel level which represents a
strong baseline for the challenging 45-way land use classification problem
especially given the noisiness of the image data.