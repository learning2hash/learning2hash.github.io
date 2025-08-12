---
layout: publication
title: Transfer Learning For Illustration Classification
authors: Manuel Lagunas, Elena Garces
conference: 2017 Spanish Computer Graphics Conference (CEIG)
year: 2018
bibkey: lagunas2018transfer
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.02682'}]
tags: []
short_authors: Manuel Lagunas, Elena Garces
---
The field of image classification has shown an outstanding success thanks to
the development of deep learning techniques. Despite the great performance
obtained, most of the work has focused on natural images ignoring other domains
like artistic depictions. In this paper, we use transfer learning techniques to
propose a new classification network with better performance in illustration
images. Starting from the deep convolutional network VGG19, pre-trained with
natural images, we propose two novel models which learn object representations
in the new domain. Our optimized network will learn new low-level features of
the images (colours, edges, textures) while keeping the knowledge of the
objects and shapes that it already learned from the ImageNet dataset. Thus,
requiring much less data for the training. We propose a novel dataset of
illustration images labelled by content where our optimized architecture
achieves \(\textbf\{86.61%\}\) of top-1 and \(\textbf\{97.21%\}\) of top-5 precision.
We additionally demonstrate that our model is still able to recognize objects
in photographs.