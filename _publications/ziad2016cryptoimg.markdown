---
layout: publication
title: 'Cryptoimg: Privacy Preserving Processing Over Encrypted Images'
authors: M. Tarek Ibn Ziad, Amr Alanwar, Moustafa Alzantot, Mani Srivastava
conference: 2016 IEEE Conference on Communications and Network Security (CNS)
year: 2016
bibkey: ziad2016cryptoimg
citations: 37
additional_links: [{name: Code, url: 'https://github.com/TarekIbnZiad/CryptoImg)'},
  {name: Paper, url: 'https://arxiv.org/abs/1609.00881'}]
tags: []
short_authors: Ziad et al.
---
Cloud computing services provide a scalable solution for the storage and
processing of images and multimedia files. However, concerns about privacy
risks prevent users from sharing their personal images with third-party
services. In this paper, we describe the design and implementation of
CryptoImg, an open source library (Source at
https://github.com/TarekIbnZiad/CryptoImg) of modular privacy preserving image
processing operations over encrypted images. By using homomorphic encryption,
CryptoImg allows the users to delegate their image processing operations to
remote servers without any privacy concerns. Currently, CryptoImg supports a
subset of the most frequently used image processing operations such as image
adjustment, spatial filtering, edge sharpening, histogram equalization and
others. We implemented our library as an extension to the popular computer
vision library OpenCV. CryptoImg can be used from either mobile or desktop
clients. Our experimental results demonstrate that CryptoImg is efficient while
performing operations over encrypted images with negligible error and
reasonable time overheads on the supported platforms