---
layout: publication
title: Privacy-preserving Image Sharing Via Sparsifying Layers On Convolutional Groups
authors: Sohrab Ferdowsi, Behrooz Razeghi, Taras Holotyak, Flavio P. Calmon, Slava
  Voloshynovskiy
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2020
bibkey: ferdowsi2020privacy
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01469'}]
tags: ["ICASSP", "Privacy & Security"]
short_authors: Ferdowsi et al.
---
We propose a practical framework to address the problem of privacy-aware
image sharing in large-scale setups. We argue that, while compactness is always
desired at scale, this need is more severe when trying to furthermore protect
the privacy-sensitive content. We therefore encode images, such that, from one
hand, representations are stored in the public domain without paying the huge
cost of privacy protection, but ambiguated and hence leaking no discernible
content from the images, unless a combinatorially-expensive guessing mechanism
is available for the attacker. From the other hand, authorized users are
provided with very compact keys that can easily be kept secure. This can be
used to disambiguate and reconstruct faithfully the corresponding
access-granted images. We achieve this with a convolutional autoencoder of our
design, where feature maps are passed independently through sparsifying
transformations, providing multiple compact codes, each responsible for
reconstructing different attributes of the image. The framework is tested on a
large-scale database of images with public implementation available.