---
layout: publication
title: 'COIN: Compression With Implicit Neural Representations'
authors: "Emilien Dupont, Adam Goli\u0144ski, Milad Alizadeh, Yee Whye Teh, Arnaud\
  \ Doucet"
conference: Arxiv
year: 2021
bibkey: dupont2021coin
citations: 86
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.03123'}]
tags: []
short_authors: Dupont et al.
---
We propose a new simple approach for image compression: instead of storing
the RGB values for each pixel of an image, we store the weights of a neural
network overfitted to the image. Specifically, to encode an image, we fit it
with an MLP which maps pixel locations to RGB values. We then quantize and
store the weights of this MLP as a code for the image. To decode the image, we
simply evaluate the MLP at every pixel location. We found that this simple
approach outperforms JPEG at low bit-rates, even without entropy coding or
learning a distribution over weights. While our framework is not yet
competitive with state of the art compression methods, we show that it has
various attractive properties which could make it a viable alternative to other
neural data compression approaches.