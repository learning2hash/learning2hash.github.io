---
layout: publication
title: Iterative Object And Part Transfer For Fine-grained Recognition
authors: Zhiqiang Shen, Yu-Gang Jiang, Dequan Wang, Xiangyang Xue
conference: 2017 IEEE International Conference on Multimedia and Expo (ICME)
year: 2017
bibkey: shen2017iterative
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.09983'}]
tags: []
short_authors: Shen et al.
---
The aim of fine-grained recognition is to identify sub-ordinate categories in
images like different species of birds. Existing works have confirmed that, in
order to capture the subtle differences across the categories, automatic
localization of objects and parts is critical. Most approaches for object and
part localization relied on the bottom-up pipeline, where thousands of region
proposals are generated and then filtered by pre-trained object/part models.
This is computationally expensive and not scalable once the number of
objects/parts becomes large. In this paper, we propose a nonparametric
data-driven method for object and part localization. Given an unlabeled test
image, our approach transfers annotations from a few similar images retrieved
in the training set. In particular, we propose an iterative transfer strategy
that gradually refine the predicted bounding boxes. Based on the located
objects and parts, deep convolutional features are extracted for recognition.
We evaluate our approach on the widely-used CUB200-2011 dataset and a new and
large dataset called Birdsnap. On both datasets, we achieve better results than
many state-of-the-art approaches, including a few using oracle (manually
annotated) bounding boxes in the test images.