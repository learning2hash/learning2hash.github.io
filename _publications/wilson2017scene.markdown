---
layout: publication
title: Scene Recognition By Combining Local And Global Image Descriptors
authors: Jobin Wilson, Muhammad Arif
conference: Arxiv
year: 2017
bibkey: wilson2017scene
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.06850'}]
tags: []
short_authors: Jobin Wilson, Muhammad Arif
---
Object recognition is an important problem in computer vision, having diverse
applications. In this work, we construct an end-to-end scene recognition
pipeline consisting of feature extraction, encoding, pooling and
classification. Our approach simultaneously utilize global feature descriptors
as well as local feature descriptors from images, to form a hybrid feature
descriptor corresponding to each image. We utilize DAISY features associated
with key points within images as our local feature descriptor and histogram of
oriented gradients (HOG) corresponding to an entire image as a global
descriptor. We make use of a bag-of-visual-words encoding and apply Mini- Batch
K-Means algorithm to reduce the complexity of our feature encoding scheme. A
2-level pooling procedure is used to combine DAISY and HOG features
corresponding to each image. Finally, we experiment with a multi-class SVM
classifier with several kernels, in a cross-validation setting, and tabulate
our results on the fifteen scene categories dataset. The average accuracy of
our model was 76.4% in the case of a 40%-60% random split of images into
training and testing datasets respectively. The primary objective of this work
is to clearly outline the practical implementation of a basic
screne-recognition pipeline having a reasonable accuracy, in python, using
open-source libraries. A full implementation of the proposed model is available
in our github repository.