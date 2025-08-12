---
layout: publication
title: Insect Pest Image Detection And Recognition Based On Bio-inspired Methods
authors: Loris Nanni, Gianluca Maguolo, Fabio Pancino
conference: Biosystems Engineering
year: 2018
bibkey: nanni2018insect
citations: 152
additional_links: [{name: Code, url: 'https://github.com/LorisNanni/'}, {name: Paper,
    url: 'https://arxiv.org/abs/1910.00296'}]
tags: ["Datasets", "Evaluation"]
short_authors: Loris Nanni, Gianluca Maguolo, Fabio Pancino
---
Insect pests recognition is necessary for crop protection in many areas of
the world. In this paper we propose an automatic classifier based on the fusion
between saliency methods and convolutional neural networks. Saliency methods
are famous image processing algorithms that highlight the most relevant pixels
of an image. In this paper, we use three different saliency methods as image
preprocessing and create three different images for every saliency method.
Hence, we create 3x3=9 new images for every original image to train different
convolutional neural networks. We evaluate the performance of every
preprocessing/network couple and we also evaluate the performance of their
ensemble. We test our approach on both a small dataset and the large IP102
dataset. Our best ensembles reaches the state of the art accuracy on both the
smaller dataset (92.43%) and the IP102 dataset (61.93%), approaching the
performance of human experts on the smaller one. Besides, we share our MATLAB
code at: https://github.com/LorisNanni/.