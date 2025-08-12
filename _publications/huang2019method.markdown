---
layout: publication
title: A Method For Identifying Origin Of Digital Images Using A Convolution Neural
  Network
authors: Rong Huang, Fuming Fang, Huy H. Nguyen, Junichi Yamagishi, Isao Echizen
conference: Arxiv
year: 2020
bibkey: huang2019method
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.00655'}]
tags: []
short_authors: Huang et al.
---
The rapid development of deep learning techniques has created new challenges
in identifying the origin of digital images because generative adversarial
networks and variational autoencoders can create plausible digital images whose
contents are not present in natural scenes. In this paper, we consider the
origin that can be broken down into three categories: natural photographic
image (NPI), computer generated graphic (CGG), and deep network generated image
(DGI). A method is presented for effectively identifying the origin of digital
images that is based on a convolutional neural network (CNN) and uses a
local-to-global framework to reduce training complexity. By feeding labeled
data, the CNN is trained to predict the origin of local patches cropped from an
image. The origin of the full-size image is then determined by majority voting.
Unlike previous forensic methods, the CNN takes the raw pixels as input without
the aid of "residual map". Experimental results revealed that not only the
high-frequency components but also the middle-frequency ones contribute to
origin identification. The proposed method achieved up to 95.21% identification
accuracy and behaved robustly against several common post-processing operations
including JPEG compression, scaling, geometric transformation, and contrast
stretching. The quantitative results demonstrate that the proposed method is
more effective than handcrafted feature-based methods.