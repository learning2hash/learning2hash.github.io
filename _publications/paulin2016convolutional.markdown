---
layout: publication
title: 'Convolutional Patch Representations For Image Retrieval: An Unsupervised Approach'
authors: Paulin et al.
conference: International Journal of Computer Vision
year: 2016
bibkey: paulin2016convolutional
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.00438'}]
tags: ["Supervised", "Image-Retrieval", "Unsupervised"]
---
Convolutional neural networks (CNNs) have recently received a lot of
attention due to their ability to model local stationary structures in natural
images in a multi-scale fashion, when learning all model parameters with
supervision. While excellent performance was achieved for image classification
when large amounts of labeled visual data are available, their success for
un-supervised tasks such as image retrieval has been moderate so far. Our paper
focuses on this latter setting and explores several methods for learning patch
descriptors without supervision with application to matching and instance-level
retrieval. To that effect, we propose a new family of convolutional descriptors
for patch representation , based on the recently introduced convolutional
kernel networks. We show that our descriptor, named Patch-CKN, performs better
than SIFT as well as other convolutional networks learned by artificially
introducing supervision and is significantly faster to train. To demonstrate
its effectiveness, we perform an extensive evaluation on standard benchmarks
for patch and image retrieval where we obtain state-of-the-art results. We also
introduce a new dataset called RomePatches, which allows to simultaneously
study descriptor performance for patch and image retrieval.