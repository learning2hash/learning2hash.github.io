---
layout: publication
title: An Adaptive Descriptor Design For Object Recognition In The Wild
authors: Zhenyu Guo, Z. Jane Wang
conference: 2013 IEEE International Conference on Computer Vision
year: 2013
bibkey: guo2013adaptive
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1305.0311'}]
tags: ["Evaluation"]
short_authors: Zhenyu Guo, Z. Jane Wang
---
Digital images nowadays have various styles of appearance, in the aspects of
color tones, contrast, vignetting, and etc. These 'picture styles' are directly
related to the scene radiance, image pipeline of the camera, and post
processing functions. Due to the complexity and nonlinearity of these causes,
popular gradient-based image descriptors won't be invariant to different
picture styles, which will decline the performance of object recognition. Given
that images shared online or created by individual users are taken with a wide
range of devices and may be processed by various post processing functions, to
find a robust object recognition system is useful and challenging. In this
paper, we present the first study on the influence of picture styles for object
recognition, and propose an adaptive approach based on the kernel view of
gradient descriptors and multiple kernel learning, without estimating or
specifying the styles of images used in training and testing. We conduct
experiments on Domain Adaptation data set and Oxford Flower data set. The
experiments also include several variants of the flower data set by processing
the images with popular photo effects. The results demonstrate that our
proposed method improve from standard descriptors in all cases.