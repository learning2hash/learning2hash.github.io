---
layout: publication
title: Boosting Cnn-based Primary Quantization Matrix Estimation Of Double JPEG Images
  Via A Classification-like Architecture
authors: Benedetta Tondi, Andrea Costranzo, Dequ Huang, Bin Li
conference: EURASIP Journal on Information Security
year: 2021
bibkey: tondi2020boosting
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.00468'}]
tags: ["Quantization"]
short_authors: Tondi et al.
---
Estimating the primary quantization matrix of double JPEG compressed images
is a problem of relevant importance in image forensics since it allows to infer
important information about the past history of an image. In addition, the
inconsistencies of the primary quantization matrices across different image
regions can be used to localize splicing in double JPEG tampered images.
Traditional model-based approaches work under specific assumptions on the
relationship between the first and second compression qualities and on the
alignment of the JPEG grid. Recently, a deep learning-based estimator capable
to work under a wide variety of conditions has been proposed, that outperforms
tailored existing methods in most of the cases. The method is based on a
Convolutional Neural Network (CNN) that is trained to solve the estimation as a
standard regression problem. By exploiting the integer nature of the
quantization coefficients, in this paper, we propose a deep learning technique
that performs the estimation by resorting to a simil-classification
architecture. The CNN is trained with a loss function that takes into account
both the accuracy and the Mean Square Error (MSE) of the estimation. Results
confirm the superior performance of the proposed technique, compared to the
state-of-the art methods based on statistical analysis and, in particular, deep
learning regression. Moreover, the capability of the method to work under
general operative conditions, regarding the alignment of the second compression
grid with the one of first compression and the combinations of the JPEG
qualities of former and second compression, is very relevant in practical
applications, where these information are unknown a priori.