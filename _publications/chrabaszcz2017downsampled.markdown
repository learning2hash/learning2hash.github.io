---
layout: publication
title: A Downsampled Variant Of Imagenet As An Alternative To The CIFAR Datasets
authors: Patryk Chrabaszcz, Ilya Loshchilov, Frank Hutter
conference: Arxiv
year: 2017
bibkey: chrabaszcz2017downsampled
citations: 389
additional_links: [{name: Code, url: 'https://github.com/PatrykChrabaszcz/Imagenet32_Scripts'},
  {name: Paper, url: 'https://arxiv.org/abs/1707.08819'}]
tags: ["Datasets"]
short_authors: Patryk Chrabaszcz, Ilya Loshchilov, Frank Hutter
---
The original ImageNet dataset is a popular large-scale benchmark for training
Deep Neural Networks. Since the cost of performing experiments (e.g, algorithm
design, architecture search, and hyperparameter tuning) on the original dataset
might be prohibitive, we propose to consider a downsampled version of ImageNet.
In contrast to the CIFAR datasets and earlier downsampled versions of ImageNet,
our proposed ImageNet32\(\times\)32 (and its variants ImageNet64\(\times\)64 and
ImageNet16\(\times\)16) contains exactly the same number of classes and images as
ImageNet, with the only difference that the images are downsampled to
32\(\times\)32 pixels per image (64\(\times\)64 and 16\(\times\)16 pixels for the
variants, respectively). Experiments on these downsampled variants are
dramatically faster than on the original ImageNet and the characteristics of
the downsampled datasets with respect to optimal hyperparameters appear to
remain similar. The proposed datasets and scripts to reproduce our results are
available at http://image-net.org/download-images and
https://github.com/PatrykChrabaszcz/Imagenet32_Scripts