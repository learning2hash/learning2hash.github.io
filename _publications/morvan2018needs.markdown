---
layout: publication
title: On The Needs For Rotations In Hypercubic Quantization Hashing
authors: "Morvan Anne, Souloumiac Antoine, Choromanski Krzysztof, Gouy-pailler C\xE9\
  dric, Atif Jamal"
conference: Arxiv
year: 2018
bibkey: morvan2018needs
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.03936'}]
tags: ["Hashing Methods", "Quantization"]
short_authors: Morvan et al.
---
The aim of this paper is to endow the well-known family of hypercubic
quantization hashing methods with theoretical guarantees. In hypercubic
quantization, applying a suitable (random or learned) rotation after
dimensionality reduction has been experimentally shown to improve the results
accuracy in the nearest neighbors search problem. We prove in this paper that
the use of these rotations is optimal under some mild assumptions: getting
optimal binary sketches is equivalent to applying a rotation uniformizing the
diagonal of the covariance matrix between data points. Moreover, for two closed
points, the probability to have dissimilar binary sketches is upper bounded by
a factor of the initial distance between the data points. Relaxing these
assumptions, we obtain a general concentration result for random matrices. We
also provide some experiments illustrating these theoretical points and compare
a set of algorithms in both the batch and online settings.