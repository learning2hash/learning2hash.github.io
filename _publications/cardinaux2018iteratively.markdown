---
layout: publication
title: Iteratively Training Look-up Tables For Network Quantization
authors: "Fabien Cardinaux, Stefan Uhlich, Kazuki Yoshiyama, Javier Alonso Garc\xED\
  a, Stephen Tiedemann, Thomas Kemp, Akira Nakamura"
conference: IEEE Journal of Selected Topics in Signal Processing
year: 2020
bibkey: cardinaux2018iteratively
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.05355'}]
tags: ["Quantization"]
short_authors: Cardinaux et al.
---
Operating deep neural networks on devices with limited resources requires the
reduction of their memory footprints and computational requirements. In this
paper we introduce a training method, called look-up table quantization, LUT-Q,
which learns a dictionary and assigns each weight to one of the dictionary's
values. We show that this method is very flexible and that many other
techniques can be seen as special cases of LUT-Q. For example, we can constrain
the dictionary trained with LUT-Q to generate networks with pruned weight
matrices or restrict the dictionary to powers-of-two to avoid the need for
multiplications. In order to obtain fully multiplier-less networks, we also
introduce a multiplier-less version of batch normalization. Extensive
experiments on image recognition and object detection tasks show that LUT-Q
consistently achieves better performance than other methods with the same
quantization bitwidth.