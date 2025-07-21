---
layout: publication
title: Unsupervised Semantic Deep Hashing
authors: Jin Sheng
conference: Neurocomputing
year: 2019
bibkey: jin2019unsupervised
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.06911'}]
tags: ["Hashing Methods", "Neural Hashing", "Unsupervised", "Supervised"]
---
In recent years, deep hashing methods have been proved to be efficient since
it employs convolutional neural network to learn features and hashing codes
simultaneously. However, these methods are mostly supervised. In real-world
application, it is a time-consuming and overloaded task for annotating a large
number of images. In this paper, we propose a novel unsupervised deep hashing
method for large-scale image retrieval. Our method, namely unsupervised
semantic deep hashing (\textbf\{USDH\}), uses semantic information preserved in
the CNN feature layer to guide the training of network. We enforce four
criteria on hashing codes learning based on VGG-19 model: 1) preserving
relevant information of feature space in hashing space; 2) minimizing
quantization loss between binary-like codes and hashing codes; 3) improving the
usage of each bit in hashing codes by using maximum information entropy, and 4)
invariant to image rotation. Extensive experiments on CIFAR-10, NUSWIDE have
demonstrated that \textbf\{USDH\} outperforms several state-of-the-art
unsupervised hashing methods for image retrieval. We also conduct experiments
on Oxford 17 datasets for fine-grained classification to verify its efficiency
for other computer vision tasks.