---
layout: publication
title: Supervised Discrete Hashing With Relaxation
authors: Jie Gui, Tongliang Liu, Zhenan Sun, Dacheng Tao, Tieniu Tan
conference: Arxiv
year: 2019
citations: 70
bibkey: gui2019supervised
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.03549'}]
tags: [Hashing Methods, Supervised, Benchmarks and Datasets]
---
Data-dependent hashing has recently attracted attention due to being able to
support efficient retrieval and storage of high-dimensional data such as
documents, images, and videos. In this paper, we propose a novel learning-based
hashing method called "Supervised Discrete Hashing with Relaxation" (SDHR)
based on "Supervised Discrete Hashing" (SDH). SDH uses ordinary least squares
regression and traditional zero-one matrix encoding of class label information
as the regression target (code words), thus fixing the regression target. In
SDHR, the regression target is instead optimized. The optimized regression
target matrix satisfies a large margin constraint for correct classification of
each example. Compared with SDH, which uses the traditional zero-one matrix,
SDHR utilizes the learned regression target matrix and, therefore, more
accurately measures the classification error of the regression model and is
more flexible. As expected, SDHR generally outperforms SDH. Experimental
results on two large-scale image datasets (CIFAR-10 and MNIST) and a
large-scale and challenging face dataset (FRGC) demonstrate the effectiveness
and efficiency of SDHR.