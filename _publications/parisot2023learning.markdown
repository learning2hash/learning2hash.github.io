---
layout: publication
title: Learning To Name Classes For Vision And Language Models
authors: Sarah Parisot, Yongxin Yang, Steven McDonagh
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: parisot2023learning
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.01830'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Sarah Parisot, Yongxin Yang, Steven McDonagh
---
Large scale vision and language models can achieve impressive zero-shot
recognition performance by mapping class specific text queries to image
content. Two distinct challenges that remain however, are high sensitivity to
the choice of handcrafted class names that define queries, and the difficulty
of adaptation to new, smaller datasets. Towards addressing these problems, we
propose to leverage available data to learn, for each class, an optimal word
embedding as a function of the visual content. By learning new word embeddings
on an otherwise frozen model, we are able to retain zero-shot capabilities for
new classes, easily adapt models to new datasets, and adjust potentially
erroneous, non-descriptive or ambiguous class names. We show that our solution
can easily be integrated in image classification and object detection
pipelines, yields significant performance gains in multiple scenarios and
provides insights into model biases and labelling errors.