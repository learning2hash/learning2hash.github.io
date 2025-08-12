---
layout: publication
title: 'Cat: Weakly Supervised Object Detection With Category Transfer'
authors: Tianyue Cao, Lianyu Du, Xiaoyun Zhang, Siheng Chen, Ya Zhang, Yan-Feng Wang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: cao2021cat
citations: 19
additional_links: [{name: Code, url: 'https://github.com/MediaBrain-SJTU/CaT'}, {
    name: Paper, url: 'https://arxiv.org/abs/2108.07487'}]
tags: ["ICCV", "Supervised"]
short_authors: Cao et al.
---
A large gap exists between fully-supervised object detection and
weakly-supervised object detection. To narrow this gap, some methods consider
knowledge transfer from additional fully-supervised dataset. But these methods
do not fully exploit discriminative category information in the
fully-supervised dataset, thus causing low mAP. To solve this issue, we propose
a novel category transfer framework for weakly supervised object detection. The
intuition is to fully leverage both visually-discriminative and
semantically-correlated category information in the fully-supervised dataset to
enhance the object-classification ability of a weakly-supervised detector. To
handle overlapping category transfer, we propose a double-supervision mean
teacher to gather common category information and bridge the domain gap between
two datasets. To handle non-overlapping category transfer, we propose a
semantic graph convolutional network to promote the aggregation of semantic
features between correlated categories. Experiments are conducted with Pascal
VOC 2007 as the target weakly-supervised dataset and COCO as the source
fully-supervised dataset. Our category transfer framework achieves 63.5% mAP
and 80.3% CorLoc with 5 overlapping categories between two datasets, which
outperforms the state-of-the-art methods. Codes are avaliable at
https://github.com/MediaBrain-SJTU/CaT.