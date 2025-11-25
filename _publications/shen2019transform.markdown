---
layout: publication
title: Transform-invariant Convolutional Neural Networks For Image Classification
  And Search
authors: Xu Shen, Xinmei Tian, Anfeng He, Shaoyan Sun, Dacheng Tao
conference: Arxiv
year: 2019
bibkey: shen2019transform
citations: 0
additional_links: [{name: Code, url: 'https://github.com/jasonustc/caffe-multigpu/tree/TICNN'},
  {name: Paper, url: 'https://arxiv.org/abs/1912.01447'}]
tags: ["Image Retrieval", "Robustness"]
short_authors: Shen et al.
---
Convolutional neural networks (CNNs) have achieved state-of-the-art results
on many visual recognition tasks. However, current CNN models still exhibit a
poor ability to be invariant to spatial transformations of images. Intuitively,
with sufficient layers and parameters, hierarchical combinations of convolution
(matrix multiplication and non-linear activation) and pooling operations should
be able to learn a robust mapping from transformed input images to
transform-invariant representations. In this paper, we propose randomly
transforming (rotation, scale, and translation) feature maps of CNNs during the
training stage. This prevents complex dependencies of specific rotation, scale,
and translation levels of training images in CNN models. Rather, each
convolutional kernel learns to detect a feature that is generally helpful for
producing the transform-invariant answer given the combinatorially large
variety of transform levels of its input feature maps. In this way, we do not
require any extra training supervision or modification to the optimization
process and training images. We show that random transformation provides
significant improvements of CNNs on many benchmark tasks, including small-scale
image recognition, large-scale image recognition, and image retrieval. The code
is available at https://github.com/jasonustc/caffe-multigpu/tree/TICNN.