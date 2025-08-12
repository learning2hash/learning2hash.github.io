---
layout: publication
title: 'Rethinking Annotation For Object Detection: Is Annotating Small-size Instances
  Worth Its Cost?'
authors: Yusuke Hosoya, Masanori Suganuma, Takayuki Okatani
conference: Arxiv
year: 2024
bibkey: hosoya2024rethinking
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05611'}]
tags: ["Datasets", "Evaluation"]
short_authors: Yusuke Hosoya, Masanori Suganuma, Takayuki Okatani
---
Detecting objects occupying only small areas in an image is difficult, even
for humans. Therefore, annotating small-size object instances is hard and thus
costly. This study questions common sense by asking the following: is
annotating small-size instances worth its cost? We restate it as the following
verifiable question: can we detect small-size instances with a detector trained
using training data free of small-size instances? We evaluate a method that
upscales input images at test time and a method that downscales images at
training time. The experiments conducted using the COCO dataset show the
following. The first method, together with a remedy to narrow the domain gap
between training and test inputs, achieves at least comparable performance to
the baseline detector trained using complete training data. Although the method
needs to apply the same detector twice to an input image with different
scaling, we show that its distillation yields a single-path detector that
performs equally well to the same baseline detector. These results point to the
necessity of rethinking the annotation of training data for object detection.