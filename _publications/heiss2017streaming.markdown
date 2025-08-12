---
layout: publication
title: Streaming Algorithm For Euler Characteristic Curves Of Multidimensional Images
authors: Teresa Heiss, Hubert Wagner
conference: Lecture Notes in Computer Science
year: 2017
bibkey: heiss2017streaming
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.02045'}]
tags: []
short_authors: Teresa Heiss, Hubert Wagner
---
We present an efficient algorithm to compute Euler characteristic curves of
gray scale images of arbitrary dimension. In various applications the Euler
characteristic curve is used as a descriptor of an image.
  Our algorithm is the first streaming algorithm for Euler characteristic
curves. The usage of streaming removes the necessity to store the entire image
in RAM. Experiments show that our implementation handles terabyte scale images
on commodity hardware. Due to lock-free parallelism, it scales well with the
number of processor cores. Our software---CHUNKYEuler---is available as open
source on Bitbucket.
  Additionally, we put the concept of the Euler characteristic curve in the
wider context of computational topology. In particular, we explain the
connection with persistence diagrams.