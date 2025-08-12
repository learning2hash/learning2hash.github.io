---
layout: publication
title: Using Wavelets To Analyze Similarities In Image-classification Datasets
authors: Roozbeh Yousefzadeh
conference: Arxiv
year: 2020
bibkey: yousefzadeh2020using
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10257'}]
tags: ["Datasets"]
short_authors: Roozbeh Yousefzadeh
---
Deep learning image classifiers usually rely on huge training sets and their
training process can be described as learning the similarities and differences
among training images. But, images in large training sets are not usually
studied from this perspective and fine-level similarities and differences among
images is usually overlooked. This is due to lack of fast and efficient
computational methods to analyze the contents of these datasets. Some studies
aim to identify the influential and redundant training images, but such methods
require a model that is already trained on the entire training set. Here, using
image processing and numerical analysis tools we develop a practical and fast
method to analyze the similarities in image classification datasets. We show
that such analysis can provide valuable insights about the datasets and the
classification task at hand, prior to training a model. Our method uses wavelet
decomposition of images and other numerical analysis tools, with no need for a
pre-trained model. Interestingly, the results we obtain corroborate the
previous results in the literature that analyzed the similarities using
pre-trained CNNs. We show that similar images in standard datasets (such as
CIFAR) can be identified in a few seconds, a significant speed-up compared to
alternative methods in the literature. By removing the computational speed
obstacle, it becomes practical to gain new insights about the contents of
datasets and the models trained on them. We show that similarities between
training and testing images may provide insights about the generalization of
models. Finally, we investigate the similarities between images in relation to
decision boundaries of a trained model.