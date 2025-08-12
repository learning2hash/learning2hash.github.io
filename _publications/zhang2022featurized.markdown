---
layout: publication
title: Featurized Query R-CNN
authors: Wenqiang Zhang, Tianheng Cheng, Xinggang Wang, Shaoyu Chen, Qian Zhang, Wenyu
  Liu
conference: Arxiv
year: 2022
bibkey: zhang2022featurized
citations: 0
additional_links: [{name: Code, url: 'https://github.com/hustvl/Featurized-QueryRCNN'},
  {name: Paper, url: 'https://arxiv.org/abs/2206.06258'}]
tags: []
short_authors: Zhang et al.
---
The query mechanism introduced in the DETR method is changing the paradigm of
object detection and recently there are many query-based methods have obtained
strong object detection performance. However, the current query-based detection
pipelines suffer from the following two issues. Firstly, multi-stage decoders
are required to optimize the randomly initialized object queries, incurring a
large computation burden. Secondly, the queries are fixed after training,
leading to unsatisfying generalization capability. To remedy the above issues,
we present featurized object queries predicted by a query generation network in
the well-established Faster R-CNN framework and develop a Featurized Query
R-CNN. Extensive experiments on the COCO dataset show that our Featurized Query
R-CNN obtains the best speed-accuracy trade-off among all R-CNN detectors,
including the recent state-of-the-art Sparse R-CNN detector. The code is
available at \{https://github.com/hustvl/Featurized-QueryRCNN.