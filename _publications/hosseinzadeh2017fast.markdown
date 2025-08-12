---
layout: publication
title: Fast Shadow Detection From A Single Image Using A Patched Convolutional Neural
  Network
authors: Sepideh Hosseinzadeh, Moein Shakeri, Hong Zhang
conference: 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2018
bibkey: hosseinzadeh2017fast
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.09283'}]
tags: ["IROS"]
short_authors: Sepideh Hosseinzadeh, Moein Shakeri, Hong Zhang
---
In recent years, various shadow detection methods from a single image have
been proposed and used in vision systems; however, most of them are not
appropriate for the robotic applications due to the expensive time complexity.
This paper introduces a fast shadow detection method using a deep learning
framework, with a time cost that is appropriate for robotic applications. In
our solution, we first obtain a shadow prior map with the help of multi-class
support vector machine using statistical features. Then, we use a semantic-
aware patch-level Convolutional Neural Network that efficiently trains on
shadow examples by combining the original image and the shadow prior map.
Experiments on benchmark datasets demonstrate the proposed method significantly
decreases the time complexity of shadow detection, by one or two orders of
magnitude compared with state-of-the-art methods, without losing accuracy.