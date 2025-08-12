---
layout: publication
title: Can Image Retrieval Help Visual Saliency Detection?
authors: Shuang Li, Peter Mathews
conference: Arxiv
year: 2017
bibkey: li2017can
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08172'}]
tags: ["Image Retrieval"]
short_authors: Shuang Li, Peter Mathews
---
We propose a novel image retrieval framework for visual saliency detection
using information about salient objects contained within bounding box
annotations for similar images. For each test image, we train a customized SVM
from similar example images to predict the saliency values of its object
proposals and generate an external saliency map (ES) by aggregating the
regional scores. To overcome limitations caused by the size of the training
dataset, we also propose an internal optimization module which computes an
internal saliency map (IS) by measuring the low-level contrast information of
the test image. The two maps, ES and IS, have complementary properties so we
take a weighted combination to further improve the detection performance.
Experimental results on several challenging datasets demonstrate that the
proposed algorithm performs favorably against the state-of-the-art methods.