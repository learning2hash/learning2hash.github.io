---
layout: publication
title: 'Dilated Convolution With Learnable Spacings: Beyond Bilinear Interpolation'
authors: "Ismail Khalfaoui-Hassani, Thomas Pellegrini, Timoth\xE9e Masquelier"
conference: Arxiv
year: 2023
bibkey: khalfaouihassani2023dilated
citations: 1
additional_links: [{name: Code, url: 'https://github.com/K-H-Ismail/Dilated-Convolution-with-Learnable-Spacings-PyTorch'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.00817'}]
tags: []
short_authors: "Ismail Khalfaoui-Hassani, Thomas Pellegrini, Timoth\xE9e Masquelier"
---
Dilated Convolution with Learnable Spacings (DCLS) is a recently proposed
variation of the dilated convolution in which the spacings between the non-zero
elements in the kernel, or equivalently their positions, are learnable.
Non-integer positions are handled via interpolation. Thanks to this trick,
positions have well-defined gradients. The original DCLS used bilinear
interpolation, and thus only considered the four nearest pixels. Yet here we
show that longer range interpolations, and in particular a Gaussian
interpolation, allow improving performance on ImageNet1k classification on two
state-of-the-art convolutional architectures (ConvNeXt and Conv\-Former),
without increasing the number of parameters. The method code is based on
PyTorch and is available at
https://github.com/K-H-Ismail/Dilated-Convolution-with-Learnable-Spacings-PyTorch