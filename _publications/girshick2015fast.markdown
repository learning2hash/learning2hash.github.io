---
layout: publication
title: Fast R-CNN
authors: Ross Girshick
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: girshick2015fast
citations: 24265
additional_links: [{name: Code, url: 'https://github.com/rbgirshick/fast-rcnn'}, {
    name: Paper, url: 'https://arxiv.org/abs/1504.08083'}]
tags: ["ICCV"]
short_authors: Ross Girshick
---
This paper proposes a Fast Region-based Convolutional Network method (Fast
R-CNN) for object detection. Fast R-CNN builds on previous work to efficiently
classify object proposals using deep convolutional networks. Compared to
previous work, Fast R-CNN employs several innovations to improve training and
testing speed while also increasing detection accuracy. Fast R-CNN trains the
very deep VGG16 network 9x faster than R-CNN, is 213x faster at test-time, and
achieves a higher mAP on PASCAL VOC 2012. Compared to SPPnet, Fast R-CNN trains
VGG16 3x faster, tests 10x faster, and is more accurate. Fast R-CNN is
implemented in Python and C++ (using Caffe) and is available under the
open-source MIT License at https://github.com/rbgirshick/fast-rcnn.