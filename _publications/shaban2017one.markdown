---
layout: publication
title: One-shot Learning For Semantic Segmentation
authors: Amirreza Shaban, Shray Bansal, Zhen Liu, Irfan Essa, Byron Boots
conference: Procedings of the British Machine Vision Conference 2017
year: 2017
bibkey: shaban2017one
citations: 590
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.03410'}]
tags: []
short_authors: Shaban et al.
---
Low-shot learning methods for image classification support learning from
sparse data. We extend these techniques to support dense semantic image
segmentation. Specifically, we train a network that, given a small set of
annotated images, produces parameters for a Fully Convolutional Network (FCN).
We use this FCN to perform dense pixel-level prediction on a test image for the
new semantic class. Our architecture shows a 25% relative meanIoU improvement
compared to the best baseline methods for one-shot segmentation on unseen
classes in the PASCAL VOC 2012 dataset and is at least 3 times faster.