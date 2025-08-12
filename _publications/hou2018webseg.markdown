---
layout: publication
title: 'Webseg: Learning Semantic Segmentation From Web Searches'
authors: Qibin Hou, Ming-Ming Cheng, Jiangjiang Liu, Philip H. S. Torr
conference: Arxiv
year: 2018
bibkey: hou2018webseg
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.09859'}]
tags: ["Datasets", "Supervised"]
short_authors: Hou et al.
---
In this paper, we improve semantic segmentation by automatically learning
from Flickr images associated with a particular keyword, without relying on any
explicit user annotations, thus substantially alleviating the dependence on
accurate annotations when compared to previous weakly supervised methods.
  To solve such a challenging problem, we leverage several low-level cues (such
as saliency, edges, etc.) to help generate a proxy ground truth. Due to the
diversity of web-crawled images, we anticipate a large amount of 'label noise'
in which other objects might be present. We design an online noise filtering
scheme which is able to deal with this label noise, especially in cluttered
images. We use this filtering strategy as an auxiliary module to help assist
the segmentation network in learning cleaner proxy annotations. Extensive
experiments on the popular PASCAL VOC 2012 semantic segmentation benchmark show
surprising good results in both our WebSeg (mIoU = 57.0%) and weakly supervised
(mIoU = 63.3%) settings.