---
layout: publication
title: A Comparison Of CNN And Classic Features For Image Retrieval
authors: "Umut \xD6zayd\u0131n, Theodoros Georgiou, Michael Lew"
conference: 2019 International Conference on Content-Based Multimedia Indexing (CBMI)
year: 2019
bibkey: "\xF6zayd\u0131n2019a"
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.09300'}]
tags: [Image Retrieval, Evaluation]
short_authors: "Umut \xD6zayd\u0131n, Theodoros Georgiou, Michael Lew"
---
Feature detectors and descriptors have been successfully used for various
computer vision tasks, such as video object tracking and content-based image
retrieval. Many methods use image gradients in different stages of the
detection-description pipeline to describe local image structures. Recently,
some, or all, of these stages have been replaced by convolutional neural
networks (CNNs), in order to increase their performance. A detector is defined
as a selection problem, which makes it more challenging to implement as a CNN.
They are therefore generally defined as regressors, converting input images to
score maps and keypoints can be selected with non-maximum suppression. This
paper discusses and compares several recent methods that use CNNs for keypoint
detection. Experiments are performed both on the CNN based approaches, as well
as a selection of conventional methods. In addition to qualitative measures
defined on keypoints and descriptors, the bag-of-words (BoW) model is used to
implement an image retrieval application, in order to determine how the methods
perform in practice. The results show that each type of features are best in
different contexts.