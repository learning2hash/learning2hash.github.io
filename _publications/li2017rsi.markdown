---
layout: publication
title: 'RSI-CB: A Large Scale Remote Sensing Image Classification Benchmark Via Crowdsource
  Data'
authors: Haifeng Li, Xin Dou, Chao Tao, Zhixiang Hou, Jie Chen, Jian Peng, Min Deng,
  Ling Zhao
conference: Arxiv
year: 2017
bibkey: li2017rsi
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10450'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Li et al.
---
In recent years, deep convolutional neural network (DCNN) has seen a
breakthrough progress in natural image recognition because of three points:
universal approximation ability via DCNN, large-scale database (such as
ImageNet), and supercomputing ability powered by GPU. The remote sensing field
is still lacking a large-scale benchmark compared to ImageNet and Place2. In
this paper, we propose a remote sensing image classification benchmark (RSI-CB)
based on massive, scalable, and diverse crowdsource data. Using crowdsource
data, such as Open Street Map (OSM) data, ground objects in remote sensing
images can be annotated effectively by points of interest, vector data from
OSM, or other crowdsource data. The annotated images can be used in remote
sensing image classification tasks. Based on this method, we construct a
worldwide large-scale benchmark for remote sensing image classification. This
benchmark has two sub-datasets with 256 by 256 and 128 by 128 sizes because
different DCNNs require different image sizes. The former contains 6 categories
with 35 subclasses of more than 24,000 images. The latter contains 6 categories
with 45 subclasses of more than 36,000 images. This classification system of
ground objects is defined according to the national standard of land-use
classification in China and is inspired by the hierarchy mechanism of ImageNet.
Finally, we conduct many experiments to compare RSI-CB with the SAT-4, SAT-6,
and UC-Merced datasets on handcrafted features, such as scale-invariant feature
transform, color histogram, local binary patterns, and GIST, and classical DCNN
models, such as AlexNet, VGGNet, GoogLeNet, and ResNet.