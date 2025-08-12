---
layout: publication
title: Fisher Kernel For Deep Neural Activations
authors: Donggeun Yoo, Sunggyun Park, Joon-Young Lee, In So Kweon
conference: Arxiv
year: 2014
bibkey: yoo2014fisher
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.1628'}]
tags: []
short_authors: Yoo et al.
---
Compared to image representation based on low-level local descriptors, deep
neural activations of Convolutional Neural Networks (CNNs) are richer in
mid-level representation, but poorer in geometric invariance properties. In
this paper, we present a straightforward framework for better image
representation by combining the two approaches. To take advantages of both
representations, we propose an efficient method to extract a fair amount of
multi-scale dense local activations from a pre-trained CNN. We then aggregate
the activations by Fisher kernel framework, which has been modified with a
simple scale-wise normalization essential to make it suitable for CNN
activations. Replacing the direct use of a single activation vector with our
representation demonstrates significant performance improvements: +17.76 (Acc.)
on MIT Indoor 67 and +7.18 (mAP) on PASCAL VOC 2007. The results suggest that
our proposal can be used as a primary image representation for better
performances in visual recognition tasks.