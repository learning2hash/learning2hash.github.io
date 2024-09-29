---
layout: publication
title: Deep Supervised Hashing With Triplet Labels
authors: Wang Xiaofang, Shi Yi, Kitani Kris M.
conference: "Arxiv"
year: 2016
bibkey: wang2016deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1612.03900"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
Hashing is one of the most popular and powerful approximate nearest neighbor search techniques for large-scale image retrieval. Most traditional hashing methods first represent images as off-the-shelf visual features and then produce hashing codes in a separate stage. However off-the-shelf visual features may not be optimally compatible with the hash code learning procedure which may result in sub-optimal hash codes. Recently deep hashing methods have been proposed to simultaneously learn image features and hash codes using deep neural networks and have shown superior performance over traditional hashing methods. Most deep hashing methods are given supervised information in the form of pairwise labels or triplet labels. The current state-of-the-art deep hashing method DPSH~(citeli2015feature) which is based on pairwise labels performs image feature learning and hash code learning simultaneously by maximizing the likelihood of pairwise similarities. Inspired by DPSH~(citeli2015feature) we propose a triplet label based deep hashing method which aims to maximize the likelihood of the given triplet labels. Experimental results show that our method outperforms all the baselines on CIFAR-10 and NUS-WIDE datasets including the state-of-the-art method DPSH~(citeli2015feature) and all the previous triplet label based deep hashing methods.
