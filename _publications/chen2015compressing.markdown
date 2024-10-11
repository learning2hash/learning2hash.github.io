---
layout: publication
title: Compressing Convolutional Neural Networks
authors: Chen Wenlin, Wilson James T., Tyree Stephen, Weinberger Kilian Q., Chen Yixin
conference: "Arxiv"
year: 2015
bibkey: chen2015compressing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1506.04449"}
tags: ['ARXIV', 'CNN', 'Deep Learning', 'Supervised']
---
Convolutional neural networks (CNN) are increasingly used in many areas of computer vision. They are particularly attractive because of their ability to absorb great quantities of labeled data through millions of parameters. However, as model sizes increase, so do the storage and memory requirements of the classifiers. We present a novel network architecture, Frequency-Sensitive Hashed Nets (FreshNets), which exploits inherent redundancy in both convolutional layers and fully-connected layers of a deep learning model, leading to dramatic savings in memory and storage consumption. Based on the key observation that the weights of learned convolutional filters are typically smooth and low-frequency, we first convert filter weights to the frequency domain with a discrete cosine transform (DCT) and use a low-cost hash function to randomly group frequency parameters into hash buckets. All parameters assigned the same hash bucket share a single value learned with standard back-propagation. To further reduce model size we allocate fewer hash buckets to high-frequency components, which are generally less important. We evaluate FreshNets on eight data sets, and show that it leads to drastically better compressed performance than several relevant baselines.
